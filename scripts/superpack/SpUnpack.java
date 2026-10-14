import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.*;
import com.github.unidbg.linux.android.dvm.array.ByteArray;
import com.github.unidbg.memory.Memory;
import java.io.*;

/** Drives Facebook's own libsuperpack-jni.so (JNI API from com.facebook.superpack.*) under unidbg
 *  to unpack a .spo archive into its member files. Usage: SpUnpack <so> <rootDir> <guestPath> <outDir> */
public class SpUnpack extends AbstractJni {
    public static void main(String[] a) throws Exception {
        AndroidEmulator emu = AndroidEmulatorBuilder.for64Bit().addBackendFactory(new com.github.unidbg.arm.backend.Unicorn2Factory(false)).setProcessName("com.facebook.katana").setRootDir(new File(a[1])).build();
        emu.getSyscallHandler().setEnableThreadDispatcher(true);
        Memory mem = emu.getMemory();
        mem.setLibraryResolver(new AndroidResolver(23));
        final com.github.unidbg.Emulator<?> fe = emu;
        mem.addHookListener(new com.github.unidbg.hook.HookListener() {
            public long hook(com.github.unidbg.memory.SvcMemory svc, String lib, String sym, long old) {
                if (old == 0) System.out.println("UNRESOLVED " + lib + " " + sym);
                if ("__fread_chk".equals(sym)) {
                    // __fread_chk(buf, buflen, size, count, fp) -> fread(buf, size, count, fp)
                    final com.github.unidbg.Symbol fread = fe.getMemory().findModule("libc.so").findSymbolByName("fread", false);
                    com.github.unidbg.pointer.UnidbgPointer tr = svc.allocate(32, "__fread_chk_trampoline");
                    java.nio.ByteBuffer bb = java.nio.ByteBuffer.allocate(32).order(java.nio.ByteOrder.LITTLE_ENDIAN);
                    bb.putInt(0xAA0203E1).putInt(0xAA0303E2).putInt(0xAA0403E3).putInt(0x58000050).putInt(0xD61F0200).putInt(0xD503201F).putLong(fread.getAddress());
                    tr.write(0, bb.array(), 0, 32);
                    return tr.peer;
                }
                return 0;
            }
        });
        VM vm = emu.createDalvikVM();
        vm.setJni(new SpUnpack());
        vm.setVerbose(false);
        DalvikModule dm = vm.loadLibrary(new File(a[0]), true);
        dm.callJNI_OnLoad(emu);
        DvmClass arc = vm.resolveClass("com/facebook/superpack/SuperpackArchive");
        DvmClass fil = vm.resolveClass("com/facebook/superpack/SuperpackFile");
        long opt = System.getenv("SPRAW") != null ? Long.parseLong(System.getenv("SPRAW")) : arc.callStaticJniMethodLong(emu, "getThreadNumOption(I)J", Integer.parseInt(System.getenv().getOrDefault("SPTHREADS", "1")));
        System.out.println("threadOpt=" + opt);
        long ar = arc.callStaticJniMethodLong(emu, "readNative(Ljava/lang/String;Ljava/lang/String;J)J",
                new StringObject(vm, a[2]), new StringObject(vm, "spo"), opt);
        System.out.println("archive=" + ar);
        File out = new File(a[3]); out.mkdirs();
        while (!arc.callStaticJniMethodBoolean(emu, "isEmptyNative(J)Z", ar)) {
            long f = arc.callStaticJniMethodLong(emu, "nextNative(J)J", ar);
            DvmObject<?> nameObj = fil.callStaticJniMethodObject(emu, "getNameNative(J)Ljava/lang/String;", f);
            String name = (String) nameObj.getValue();
            int len = fil.callStaticJniMethodInt(emu, "getLengthNative(J)I", f);
            System.out.println(name + " " + len);
            try (FileOutputStream fo = new FileOutputStream(new File(out, name.replace('/', '_')))) {
                int chunk = 1 << 20;
                for (int off = 0; off < len; off += chunk) {
                    int n = Math.min(chunk, len - off);
                    ByteArray buf = new ByteArray(vm, new byte[n]);
                    vm.addLocalObject(buf);
                    fil.callStaticJniMethod(emu, "readBytesNative(JII[BI)V", f, off, n, buf, 0);
                    fo.write(buf.getValue(), 0, n);
                }
            }
            fil.callStaticJniMethod(emu, "closeNative(J)V", f);
        }
        arc.callStaticJniMethod(emu, "closeNative(J)V", ar);
        emu.close();
    }
}
