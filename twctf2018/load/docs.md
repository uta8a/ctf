# load
```
host : pwn1.chal.ctf.westerns.tokyo
port : 34835

load
```

# do
- `nc pwn1.chal.ctf.westerns.tokyo 34835`で接続してみる
```
vagrant@vagrant:~/working$ nc pwn1.chal.ctf.westerns.tokyo 34835
Load file Service
Input file name: %s
Input offset: %s
Input size: %s
You can't read this file...
```
- AAAAAAとか入れても`You can't read this file...`となって、入力値が反映されるわけでもないので静的に解析していく。
- file
```
vagrant@vagrant:~/working$ file load-ef05273401f331748cca5fcb8b14c43f80600adf4266fee4e5f250730b503f0c
load-ef05273401f331748cca5fcb8b14c43f80600adf4266fee4e5f250730b503f0c: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=a0620e5b122fd043e5a40e181f3f3adf29e6f4c1, stripped
```
- strings
```
vagrant@vagrant:~/working$ strings load-ef05273401f331748cca5fcb8b14c43f80600adf4266fee4e5f250730b503f0c
/lib64/ld-linux-x86-64.so.2
|.N=
libc.so.6
__printf_chk
puts
stdin
fgets
read
stdout
lseek
atoi
close
open
strchr
setbuf
__libc_start_main
__gmon_start__
GLIBC_2.3.4
GLIBC_2.2.5
AWAVA
AUATL
[]A\A]A^A_
Load file Service
Input file name:
Input offset:
Input size:
You can't read this file...
Load file complete!
;*3$"
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.9) 5.4.0 20160609
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
- ltraceかけながら実行しても何も出てこない
- radare2
- afl
```
[0x00400720]> afl
0x00400690    3 26           sub.__gmon_start_690
0x004006c0    1 6            sub.puts_6c0
0x004006c8    1 6            sub.setbuf_6c8
0x004006d0    1 6            sub.strchr_6d0
0x004006d8    1 6            sub.lseek_6d8
0x004006e0    1 6            sub.close_6e0
0x004006e8    1 6            sub.read_6e8
0x004006f0    1 6            sub.__libc_start_main_6f0
0x004006f8    1 6            sub.fgets_6f8
0x00400700    1 6            sub.__gmon_start_700
0x00400708    1 6            sub.__printf_chk_708
0x00400710    1 6            sub.open_710
0x00400718    1 6            sub.atoi_718
0x00400720    1 42           entry0
0x00400750    4 50   -> 41   fcn.00400750
0x004007d0    3 28           entry2.fini
0x004007f0    8 38   -> 90   entry1.init
0x00400816    1 147          main
0x004008a9    1 47           fcn.004008a9
0x004008d8    1 37           fcn.004008d8
0x004008fd    6 137          sub.You_can_t_read_this_file..._8fd
0x00400986    5 85           fcn.00400986
0x004009db    1 43           fcn.004009db
```
- fgetsとか怪しそう
- pdf main
```
[0x00400816]> pdf
/ (fcn) main 147
|   main ();
|           ; var int local_30h @ rbp-0x30
|           ; var int local_10h @ rbp-0x10
|           ; var int local_8h @ rbp-0x8
|           ; DATA XREF from entry0 (0x40073d)
|           0x00400816      55             push rbp
|           0x00400817      4889e5         mov rbp, rsp
|           0x0040081a      4883ec30       sub rsp, 0x30               ; '0'
|           0x0040081e      e886000000     call fcn.004008a9
|           0x00400823      be980a4000     mov esi, str.Load_file_Service__Input_file_name: ; 0x400a98 ; "Load file Service\nInput file name: "
|           0x00400828      bf01000000     mov edi, 1
|           0x0040082d      b800000000     mov eax, 0
|           0x00400832      e8d1feffff     call sub.__printf_chk_708
|           0x00400837      be80000000     mov esi, 0x80               ; 128
|           0x0040083c      bf40106000     mov edi, 0x601040
|           0x00400841      e840010000     call fcn.00400986
|           0x00400846      bebc0a4000     mov esi, str.Input_offset:  ; 0x400abc ; "Input offset: "
|           0x0040084b      bf01000000     mov edi, 1
|           0x00400850      b800000000     mov eax, 0
|           0x00400855      e8aefeffff     call sub.__printf_chk_708
|           0x0040085a      e87c010000     call fcn.004009db
|           0x0040085f      4898           cdqe
|           0x00400861      488945f8       mov qword [local_8h], rax
|           0x00400865      becb0a4000     mov esi, str.Input_size:    ; 0x400acb ; "Input size: "
|           0x0040086a      bf01000000     mov edi, 1
|           0x0040086f      b800000000     mov eax, 0
|           0x00400874      e88ffeffff     call sub.__printf_chk_708
|           0x00400879      e85d010000     call fcn.004009db
|           0x0040087e      4898           cdqe
|           0x00400880      488945f0       mov qword [local_10h], rax
|           0x00400884      488b4df0       mov rcx, qword [local_10h]
|           0x00400888      488b55f8       mov rdx, qword [local_8h]
|           0x0040088c      488d45d0       lea rax, [local_30h]
|           0x00400890      be40106000     mov esi, 0x601040
|           0x00400895      4889c7         mov rdi, rax
|           0x00400898      e860000000     call sub.You_can_t_read_this_file..._8fd
|           0x0040089d      e836000000     call fcn.004008d8
|           0x004008a2      b800000000     mov eax, 0
|           0x004008a7      c9             leave
\           0x004008a8      c3             ret
```
- ix
```
[0x004008d8]> ix
blksz    0x0
block    0x100
fd       3
file     load-ef05273401f331748cca5fcb8b14c43f80600adf4266fee4e5f250730b503f0c
format   elf64
iorw     false
mode     r-x
size     0x17f8
humansz  6.0K
type     EXEC (Executable file)
arch     x86
binsz    4402
bintype  elf
bits     64
canary   false
class    ELF64
crypto   false
endian   little
havecode true
intrp    /lib64/ld-linux-x86-64.so.2
lang     c
linenum  false
lsyms    false
machine  AMD x86-64 architecture
maxopsz  16
minopsz  1
nx       true
os       linux
pcalign  0
pic      false
relocs   false
relro    full
rpath    NONE
static   false
stripped true
subsys   linux
va       true
```
- `canary   false`が嬉しいくらいしかわからない…
- 調査
- `fcn.004008a9`はファイルを読み込む関数
- `fcn.00400986`でもファイル読み込みぽいことが行われている
- fcnはfunctionの意味だろうから、たぶんここの依存関係からなにかがわかるのかな…分からない。