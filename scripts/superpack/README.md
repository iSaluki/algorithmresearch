# Facebook Superpack unpacking (unsuccessful attempt)

Facebook ships almost all of its Java code as `assets/secondary-program-dex-jars/store-0.dex.spo`,
compressed with Meta's proprietary Superpack format, which only its own `libsuperpack-jni.so` can decode.
These files are the attempt to run that library under [unidbg](https://github.com/zhkl0228/unidbg) (Unicorn2 backend)
and call its JNI API (`SuperpackArchive.readNative` / `nextNative`, `SuperpackFile.readBytesNative`) the way the
app's loader does.

- `unidbg-relr.patch`: adds RELR relocation support (`DT_RELR` / `DT_ANDROID_RELR`) to unidbg's ELF loader.
  Without it, the library's `init_array` and GOT entries are unrelocated and `JNI_OnLoad` fails. Also fixes the
  build on JDK 21.
- `apply_relr.py`: alternative that pre-applies RELR relocations to a copy of the library for a fixed load base.
- `SpUnpack.java`: the harness. It enables unidbg's thread dispatcher (the decoder uses a worker thread) and
  routes `__fread_chk` through a register-shuffling trampoline to `fread`.

**Status:** the library loads and `JNI_OnLoad` succeeds. The decoder thread starts and reads the archive header,
then crashes on an unmapped read inside the decompressor. This is most likely an emulation gap in file I/O or
mmap. The Facebook section of the report is therefore based on the manifest, resources, assets, MobileConfig
flag names and the loader DEX, not on decompiled main-app code.
