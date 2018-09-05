# dec dec dec
```
dec_dec_dec
```

# do
- file
```
vagrant@vagrant:~/working$ file dec_dec_dec-c55c231bfbf686ab058bac2a56ce6cc49ae32fe086af499571e335c9f7417e5b
dec_dec_dec-c55c231bfbf686ab058bac2a56ce6cc49ae32fe086af499571e335c9f7417e5b: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0c8f77007398e1cb7857e481cff521122c1b2cb9, stripped
```
- strings
```
vagrant@vagrant:~/working$ strings dec_dec_dec-c55c231bfbf686ab058bac2a56ce6cc49ae32fe086af499571e335c9f7417e5b
/lib64/ld-linux-x86-64.so.2
libc.so.6
exit
strncpy
puts
__stack_chk_fail
strlen
malloc
__cxa_finalize
strcmp
__libc_start_main
_ITM_deregisterTMCloneTable
__gmon_start__
_Jv_RegisterClasses
_ITM_registerTMCloneTable
GLIBC_2.4
GLIBC_2.2.5
ABCDEFGHH
IJKLMNOPH
QRSTUVWXH
YZabcdefH
ghijklmnH
opqrstuvH
wxyz0123H
456789+/H
dH34%(
dH34%(
AWAVA
AUATL
[]A\A]A^A_
@25-Q44E233=,>E-M34=,,$LS5VEQ45)M2S-),7-$/3T
./dec_dec_dec flag_string_is_here
correct  :)
incorrect :(
;*3$"
GCC: (Ubuntu 6.3.0-12ubuntu2) 6.3.0 20170406
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.init
.plt
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.jcr
.dynamic
.data
.bss
.comment
```
- radare2
- [0x00000860]がすごいあやしい
```
int64_t strlen () {
    *(s) = rdi;
    rax = *(fs + 0x28);
    *(canary) = rax;
    eax = 0;
    rax = 0x4847464544434241;
    *(local_50h) = rax;
    rax = 0x504f4e4d4c4b4a49;
    *(local_48h) = rax;
    rax = 0x5857565554535251;
    *(local_40h) = rax;
    rax = 0x6665646362615a59;
    *(local_38h) = rax;
    rax = 0x6e6d6c6b6a696867;
    *(local_30h) = rax;
    rax = 0x767574737271706f;
    *(local_28h) = rax;
    rax = 0x333231307a797877;
    *(local_20h) = rax;
    rax = 0x2f2b393837363534;
    *(local_18h) = rax;
    *(local_10h) = 0;
    rax = *(s);
    rdi = rax;
...(省略))
```
- pdf
```
|           0x00000872      64488b042528.  mov rax, qword fs:[0x28]    ; [0x28:8]=0x2138 ; '(' ; "8!"
|           0x0000087b      488945f8       mov qword [canary], rax
|           0x0000087f      31c0           xor eax, eax
|           0x00000881      48b841424344.  movabs rax, 0x4847464544434241 ; 'ABCDEFGH'
|           0x0000088b      488945b0       mov qword [local_50h], rax
|           0x0000088f      48b8494a4b4c.  movabs rax, 0x504f4e4d4c4b4a49 ; 'IJKLMNOP'
|           0x00000899      488945b8       mov qword [local_48h], rax
|           0x0000089d      48b851525354.  movabs rax, 0x5857565554535251 ; 'QRSTUVWX'
|           0x000008a7      488945c0       mov qword [local_40h], rax
|           0x000008ab      48b8595a6162.  movabs rax, 0x6665646362615a59 ; 'YZabcdef'
|           0x000008b5      488945c8       mov qword [local_38h], rax
|           0x000008b9      48b86768696a.  movabs rax, 0x6e6d6c6b6a696867 ; 'ghijklmn'
|           0x000008c3      488945d0       mov qword [local_30h], rax
|           0x000008c7      48b86f707172.  movabs rax, 0x767574737271706f ; 'opqrstuv'
|           0x000008d1      488945d8       mov qword [local_28h], rax
|           0x000008d5      48b87778797a.  movabs rax, 0x333231307a797877 ; 'wxyz0123'
|           0x000008df      488945e0       mov qword [local_20h], rax
|           0x000008e3      48b834353637.  movabs rax, 0x2f2b393837363534 ; '456789+/'
```
- みたいになってて、明らかに怪しい
- でもどうすればいいのかわからない。

# 解説見た
- [参考になったwriteup](https://github.com/ccowmu/ctf_2018/tree/master/writeups/TokyoCTF2018/dec-dec-dec)、[これも](http://teppay.hatenablog.com/entry/2018/09/03/130011#dec-dec-decwarmup-reversing)
- タイトルの意味は3回decodeという意味らしい。
- 正しい入力がフラッグと思われる(正誤判定のみ行うので)
- r2で見る→`sub.strlen_860`, `sub.strlen_f59`, `sub.strlen_be7`を通している
- この三つの関数を調べる
- `sub.strlen_860`について
```
'ABCDEFGH'
'IJKLMNOP'
'QRSTUVWX'
'YZabcdef'
'ghijklmn'
'opqrstuv'
'wxyz0123'
'456789+/'
```
- やはりここが怪しくて、64文字なのでBase64を疑う
- base64と確かめるために、860を使った結果を見たいけど(具体的には860に直接変数入れて、その出力を見たい)どうやってやるのか分からない。

```
0x000010f8      488b15110f20.  mov rdx, qword str.25_Q44E233___E_M34____LS5VEQ45_M2S___7___3T ; [0x202010:8]=0x11c8 str.25_Q44E233___E_M34____LS5VEQ45_M2S___7___3T
|           0x000010ff      488b45f8       mov rax, qword [dest]
|           0x00001103      4889d6         mov rsi, rdx                ; const char *s2
|           0x00001106      4889c7         mov rdi, rax                ; const char *s1
|           0x00001109      e802f6ffff     call sym.imp.strcmp         ; int strcmp(const char *s1, const char *s2)
```
- このへんで、strcmpで比較しているのは`25_Q44E233___E_M34____LS5VEQ45_M2S___7___3T`と分かるので、これを順にdecodeしていく。(be7 -> f59 -> 860の順にdec)
