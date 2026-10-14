"""Pre-apply RELR (relative) relocations of an ARM64 ELF for a fixed load base,
for emulators whose loader lacks RELR support. Usage: apply_relr.py in.so out.so base"""
import struct, sys
data = bytearray(open(sys.argv[1], "rb").read()); base = int(sys.argv[3], 16)
e_phoff, = struct.unpack_from("<Q", data, 0x20); e_phentsize, e_phnum = struct.unpack_from("<HH", data, 0x36)
e_shoff, = struct.unpack_from("<Q", data, 0x28); e_shentsize, e_shnum = struct.unpack_from("<HH", data, 0x3a)
loads = []
for i in range(e_phnum):
    p_type, p_flags, p_off, p_vaddr, p_paddr, p_filesz, p_memsz, p_align = struct.unpack_from("<IIQQQQQQ", data, e_phoff + i * e_phentsize)
    if p_type == 1: loads.append((p_vaddr, p_off, p_filesz))
def v2o(v):
    for va, off, sz in loads:
        if va <= v < va + sz: return off + (v - va)
    raise ValueError(hex(v))
relr = None
for i in range(e_shnum):
    sh = struct.unpack_from("<IIQQQQIIQQ", data, e_shoff + i * e_shentsize)
    if sh[1] in (0x6fffff00, 19):  # SHT_ANDROID_RELR / SHT_RELR
        relr = (sh[4], sh[5])
off, size = relr; n = 0; where = 0
for k in range(size // 8):
    entry, = struct.unpack_from("<Q", data, off + 8 * k)
    if entry & 1 == 0:
        o = v2o(entry); val, = struct.unpack_from("<Q", data, o); struct.pack_into("<Q", data, o, val + base); n += 1
        where = entry + 8
    else:
        bits = entry >> 1
        for j in range(63):
            if bits & (1 << j):
                o = v2o(where + 8 * j); val, = struct.unpack_from("<Q", data, o); struct.pack_into("<Q", data, o, val + base); n += 1
        where += 63 * 8
open(sys.argv[2], "wb").write(data); print("applied", n, "RELR relocations")
