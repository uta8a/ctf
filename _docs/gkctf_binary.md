# GrowthKeysCTF Binary
- 9/11-9/25までのミニCTF、GKCTF(Binary)を行いました。
- 以下、Writeupです

# Writeup
- 環境は、Ubuntu16.04(VirtualBox, ホストはWindows10)で確認しています。
### A. Hello Friends
- よくある最初のやつです。`gkctf{hello_world}` -> AC

### B. Binary 1
- `strings`コマンドを使います。
```
$ strings bin100_1
/lib64/ld-linux-x86-64.so.2
libc.so.6
puts
__libc_start_main
__gmon_start__
GLIBC_2.2.5
AWAVA
AUATL
[]A\A]A^A_
HiddenFlag
You cannot get flag! hahaha
;*3$"
ctf4b{fl4g_n07_1n_c0d3_53gm3n7}
...
```
- `ctf4b{fl4g_n07_1n_c0d3_53gm3n7}` -> AC
- 出典: ctf4b広島2018

### C. Binary 2 [ctf4b広島2018]
- `radare2`を使います。
- `main`を見てもフラッグっぽいものは見当たらないので、`sym.genflag`など、flagが名前に含まれる怪しい関数を調べていきます。
- 文字が見つかるのでそれを直します。`section...`はASCIIの方を見ると`0x35 -> 5`と分かるので直してあげます。
```
$ r2 bin200_2
> aaaa
> afl
0x00400460    3 26           sym._init
0x00400490    1 6            sym.imp.puts
0x004004a0    1 6            sym.imp.__stack_chk_fail
0x004004b0    1 6            sym.imp.__libc_start_main
0x004004c0    1 6            sym.imp.malloc
0x004004d0    1 6            sub.__gmon_start_4d0
0x004004e0    1 41           entry0
0x00400510    4 50   -> 41   sym.deregister_tm_clones
0x00400550    3 53           sym.register_tm_clones
0x00400590    3 28           sym.__do_global_dtors_aux
0x004005b0    4 38   -> 35   entry1.init
0x004005d6    1 21           sym.main
0x004005eb    6 273          sym.genflag
0x00400700    4 101          sym.__libc_csu_init
0x00400770    1 2            sym.__libc_csu_fini
0x00400774    1 9            sym._fini
> s sym.genflag
> pdf
...
0x00400602      c645c063       mov byte [local_40h], 0x63  ; 'c' ; 99
|           0x00400606      c645c174       mov byte [local_3fh], 0x74  ; 't' ; 116
|           0x0040060a      c645c266       mov byte [local_3eh], 0x66  ; 'f' ; 102
|           0x0040060e      c645c334       mov byte [local_3dh], 0x34  ; '4' ; 52
|           0x00400612      c645c462       mov byte [local_3ch], 0x62  ; 'b' ; 98
|           0x00400616      c645c57b       mov byte [local_3bh], 0x7b  ; '{' ; 123
|           0x0040061a      c645c663       mov byte [local_3ah], 0x63  ; 'c' ; 99
|           0x0040061e      c645c734       mov byte [local_39h], 0x34  ; '4' ; 52
|           0x00400622      c645c86e       mov byte [local_38h], 0x6e  ; 'n' ; 110
|           0x00400626      c645c95f       mov byte [local_37h], 0x5f  ; '_' ; 95
|           0x0040062a      c645ca79       mov byte [local_36h], 0x79  ; 'y' ; 121
|           0x0040062e      c645cb30       mov byte [local_35h], 0x30  ; '0' ; 48
|           0x00400632      c645cc75       mov byte [local_34h], 0x75  ; 'u' ; 117
|           0x00400636      c645cd5f       mov byte [local_33h], 0x5f  ; '_' ; 95
|           0x0040063a      c645ce66       mov byte [local_32h], 0x66  ; 'f' ; 102
|           0x0040063e      c645cf31       mov byte [local_31h], 0x31  ; '1' ; 49
|           0x00400642      c645d06e       mov byte [local_30h], 0x6e  ; 'n' ; 110
|           0x00400646      c645d164       mov byte [local_2fh], 0x64  ; 'd' ; 100
|           0x0040064a      c645d25f       mov byte [local_2eh], 0x5f  ; '_' ; 95
|           0x0040064e      c645d330       mov byte [local_2dh], 0x30  ; '0' ; 48
|           0x00400652      c645d475       mov byte [local_2ch], 0x75  ; 'u' ; 117
|           0x00400656      c645d537       mov byte [local_2bh], 0x37  ; '7' ; 55
|           0x0040065a      c645d65f       mov byte [local_2ah], 0x5f  ; '_' ; 95
|           0x0040065e      c645d775       mov byte [local_29h], 0x75  ; 'u' ; 117
|           0x00400662      c645d86e       mov byte [local_28h], 0x6e  ; 'n' ; 110
|           0x00400666      c645d975       mov byte [local_27h], 0x75  ; 'u' ; 117
|           0x0040066a      c645da35       mov byte [local_26h], 0x35  ; section_end..comment
|           0x0040066e      c645db33       mov byte [local_25h], 0x33  ; '3' ; 51
|           0x00400672      c645dc64       mov byte [local_24h], 0x64  ; 'd' ; 100
|           0x00400676      c645dd5f       mov byte [local_23h], 0x5f  ; '_' ; 95
|           0x0040067a      c645de66       mov byte [local_22h], 0x66  ; 'f' ; 102
|           0x0040067e      c645df75       mov byte [local_21h], 0x75  ; 'u' ; 117
|           0x00400682      c645e06e       mov byte [local_20h], 0x6e  ; 'n' ; 110
|           0x00400686      c645e163       mov byte [local_1fh], 0x63  ; 'c' ; 99
|           0x0040068a      c645e237       mov byte [local_1eh], 0x37  ; '7' ; 55
|           0x0040068e      c645e331       mov byte [local_1dh], 0x31  ; '1' ; 49
|           0x00400692      c645e430       mov byte [local_1ch], 0x30  ; '0' ; 48
|           0x00400696      c645e56e       mov byte [local_1bh], 0x6e  ; 'n' ; 110
|           0x0040069a      c645e63f       mov byte [local_1ah], 0x3f  ; '?' ; 63
|           0x0040069e      c645e77d       mov byte [local_19h], 0x7d  ; '}' ; 125
...
```
- `ctf4b{c4n_y0u_f1nd_0u7_unu53d_func710n?}` -> AC
- 出典: ctf4b広島2018

### D. Binary 3
- デバッグモードで`radare2`を起動します
```
$ r2 -d SimpleBinary
> aaaa
> s main
> pdf
```
- 怪しい文字列を発見します
```
0x004006d1      48b87b694343.  movabs rax, 0x69732e204343697b ; '{iCC .si'
0x004006df      48b874682074.  movabs rax, 0x4620752774206874 ; 'th t'u F'
0x004006ed      48b86e7d6449.  movabs rax, 0x6167546d49647d6e ; 'n}dImTga'
0x004006fb      66c745e85268   mov word [local_18h], 0x6852 ; 'Rh'
```
- このままではフラッグっぽくないので、"処理後のスタックを見る"という典型手法を思い出して、breakpointを設置します。
```
> db 0x00400729
> dc
> pxr @ rsp
```
- 中身を見ます
```
0x7ffefdafce00  0x00007ffefdafcf38   8....... @rsp stack R W 0x7ffefdafe6c8 -->  stack R W 0x656c706d69532f2e (./SimpleBinary) -->  ascii
0x7ffefdafce08  0x000000016f736476   vdso....
0x7ffefdafce10  0x0000000000000001   ........
0x7ffefdafce18  0x0000001b0040078d   ..@.....
0x7ffefdafce20  0x74497b4654435243   CRCTF{It @rdi ascii
0x7ffefdafce28  0x6d75682061207327   's a hum ascii
0x7ffefdafce30  0x746867696e206469   id night ascii
0x7ffefdafce38  0x0000000000007d2e   .}...... ascii
0x7ffefdafce40  0x00007ffefdafcf30   0....... r13 stack R W 0x1
0x7ffefdafce48  0x2010cbacc6f98d00   .......  rcx
0x7ffefdafce50  0x0000000000400740   @.@..... @rbp (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) program R X 'push r15' 'SimpleBinary'
0x7ffefdafce58  0x00007f1cd1a00830   0.......
0x7ffefdafce60  0x0000000000000000   ........ esp
0x7ffefdafce68  0x00007ffefdafcf38   8....... stack R W 0x7ffefdafe6c8 -->  stack R W 0x656c706d69532f2e (./SimpleBinary) -->  ascii
0x7ffefdafce70  0x0000000100000000   ........
0x7ffefdafce78  0x00000000004006b3   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) main main program R X 'push rbp' 'SimpleBinary'
0x7ffefdafce80  0x0000000000000000   ........ esp
0x7ffefdafce88  0x7526e24ea3da1f02   ....N.&u
0x7ffefdafce90  0x0000000000400450   P.@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) r12 entry0 program R X 'xor ebp, ebp' 'SimpleBinary'
0x7ffefdafce98  0x00007ffefdafcf30   0....... r13 stack R W 0x1
0x7ffefdafcea0  0x0000000000000000   ........ esp
0x7ffefdafcea8  0x0000000000000000   ........ esp
0x7ffefdafceb0  0x8adb1991319a1f02   ...1....
0x7ffefdafceb8  0x8b1f418ea28a1f02   .....A..
0x7ffefdafcec0  0x0000000000000000   ........ esp
0x7ffefdafcec8  0x0000000000000000   ........ esp
0x7ffefdafced0  0x0000000000000000   ........ esp
0x7ffefdafced8  0x0000000000000001   ........
0x7ffefdafcee0  0x00000000004006b3   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) main main program R X 'push rbp' 'SimpleBinary'
0x7ffefdafcee8  0x00000000004007b0   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) r8 program R X 'ret' 'SimpleBinary'
0x7ffefdafcef0  0x0000000000000000   ........ esp
0x7ffefdafcef8  0x0000000000000000   ........ esp
```
- `CRCTF{It's a humid night.}` -> AC
- 出典: CyberRebeatCTF

### E. Binary 4
- `radare2`を使います
```
$ r2 validator
> aaaa
> s main
> pdf
|           0x0804852e      c745d035375f.  mov dword [local_30h], 0x635f3735 ; '57_c'
|           0x08048535      c745d4346c6c.  mov dword [local_2ch], 0x5f6c6c34 ; '4ll_'
|           0x0804853c      c745d86d335f.  mov dword [local_28h], 0x725f336d ; 'm3_r'
|           0x08048543      c745dc337633.  mov dword [local_24h], 0x72337633 ; '3v3r'
|           0x0804854a      c745e035335f.  mov dword [local_20h], 0x365f3335 ; '53_6'
|           0x08048551      c745e430645f.  mov dword [local_1ch], 0x665f6430 ; '0d_f'
|           0x08048558      c745e872306d.  mov dword [local_18h], 0x5f6d3072 ; 'r0m_'
|           0x0804855f      c745ec6e3077.  mov dword [local_14h], 0x5f77306e ; 'n0w_'
|           0x08048566      c745f0306e7d.  mov dword [local_10h], 0x7d6e30 ; '0n}'
```
- このまま`tjctf{ju57_c4ll_m3_r3v3r53_60d_fr0m_n0w_0n}`を入れてもWAになります。
- もう少しコードを見ていくと、`strlen` -> `strcmp`で比較していることがわかります。つまり、長さを比較したのちにそれぞれの文字を比較しているということがわかります。
- ltraceを使ってみましょう
```
$ ltrace ./validator tjctf{ju57_c4ll_m3_r3v3r53_60d_fr0m_n0w_0n}
__libc_start_main(0x80484fb, 2, 0xfffad7e4, 0x8048640 <unfinished ...>
strlen("tjctf{ju57_c4ll_m3_r3v3r53_60d_f"...)                             = 43
strcmp("tjctf{ju57_c4ll_m3_35r3v3r_60d_f"..., "tjctf{ju57_c4ll_m3_r3v3r53_60d_f"...) = -1
puts("Invalid flag."Invalid flag.
)                                                     = 14
+++ exited (status 0) +++
```
- strcmpの中身を見ると、`r3v3r53`の順番が違うことに気づきます。入れ替えます。
- `tjctf{ju57_c4ll_m3_35r3v3r_60d_fr0m_n0w_0n}` -> AC
- 出典: tjctf2018

### F. mitsu_200
- ひとまず`radare2`を起動します
```
$ r2 mitsu_200
> aaaa
> s main
> pdf
/ (fcn) main 82
|   main ();
|           ; var signed int local_4h @ rbp-0x4
|           ; STRING XREF from entry0 (0x1061)
|           0x00001139      55             push rbp
|           0x0000113a      4889e5         mov rbp, rsp
|           0x0000113d      4883ec10       sub rsp, 0x10
|           0x00001141      c745fc000000.  mov dword [local_4h], 0
|       ,=< 0x00001148      eb28           jmp 0x1172
|       |   ; CODE XREF from main (0x1176)
|      .--> 0x0000114a      8b45fc         mov eax, dword [local_4h]
|      :|   0x0000114d      4898           cdqe
|      :|   0x0000114f      488d15da2e00.  lea rdx, str.RZM_B          ; obj.flag ; 0x4030 ; "^RZM_B\f\x0efPJfXfIKPT\fWLT[\K\x18\x18\x18D"
|      :|   0x00001156      0fb60410       movzx eax, byte [rax + rdx]
|      :|   0x0000115a      83f039         xor eax, 0x39
|      :|   0x0000115d      89c1           mov ecx, eax
|      :|   0x0000115f      8b45fc         mov eax, dword [local_4h]
|      :|   0x00001162      4898           cdqe
|      :|   0x00001164      488d15c52e00.  lea rdx, str.RZM_B          ; obj.flag ; 0x4030 ; "^RZM_B\f\x0efPJfXfIKPT\fWLT[\K\x18\x18\x18D"
|      :|   0x0000116b      880c10         mov byte [rax + rdx], cl
|      :|   0x0000116e      8345fc01       add dword [local_4h], 1
|      :|   ; CODE XREF from main (0x1148)
|      :`-> 0x00001172      837dfc1d       cmp dword [local_4h], 0x1d  ; [0x1d:4]=0x40000000
|      `==< 0x00001176      7ed2           jle 0x114a
|           0x00001178      488d3d890e00.  lea rdi, str.You_could_execute_this_binary__hai_pro. ; 0x2008 ; "You could execute this binary! hai pro." ; const char *s
|           0x0000117f      e8acfeffff     call sym.imp.puts           ; int puts(const char *s)
|           0x00001184      b800000000     mov eax, 0
|           0x00001189      c9             leave
\           0x0000118a      c3             ret
```
- 眺めると、`obj.flag`になにか操作をしているようです
```
> s obj.flag
> pxr
0x00004030  0x0e0c425f4d5a525e   ^RZM_B.. @obj.flag
0x00004038  0x4b496658664a5066   fPJfXfIK @str.fPJfXfIKPT___WLT___K ascii
0x00004040  0x5b544c57665c5450   PT\fWLT[ ascii
0x00004048  0x0000441818184b5c   \K...D..
```
- アセンブラを読みます
- `mov`, `eax`, `rdx`, `lea`, `byte[rax+rdx]`などいろいろ出てくるので調べてみてください。(質問はいつでも大丈夫です)
- 簡単に説明すると、byteは配列rdx[rax]のようなもので、obj.flagに格納された値ひとつに対しxorを取って新しい文字ひとつを生成している、みたいな感じになります。
- アセンブラをpythonコードに書き直します
```
st = [0x5e, 0x52, 0x5a, 0x4d, 0x5f, 0x42, 0x0c, 0x0e, 0x66, 0x50, 0x4a, 0x66, 0x58, 0x66, 0x49, 0x4b, 0x50, 0x54, 0x5c, 0x66, 0x57, 0x4c, 0x54, 0x5b, 0x5c, 0x4b, 0x18, 0x18, 0x18, 0x44, 0x00, 0x00] # リトルエンディアン
local_4h = 0
while local_4h <= 29:
    eax = st[local_4h]
    eax ^= 0x39
    print(chr(eax))
    local_4h += 1
```
- 出力を見てやると、`gkctf{57_is_a_prime_number!!!}` -> AC
- 出典: mitsuさんの自作問題
- [+ 追記] バイナリを実行可能にする
- readelfでバイナリの情報を見る
```
vagrant@vagrant:~/gkctf/mitsu$ readelf -h mitsu_200
ELF Header:
  Magic:   7f 45 4c 46 02 01 01 00 00 00 00 00 00 00 00 00
  Class:                             ELF64
  Data:                              2's complement, little endian
  Version:                           1 (current)
  OS/ABI:                            UNIX - System V
  ABI Version:                       0
  Type:                              DYN (Shared object file)
  Machine:                           Advanced Micro Devices X86-64
  Version:                           0x1
  Entry point address:               0x0
  Start of program headers:          64 (bytes into file)
  Start of section headers:          14768 (bytes into file)
  Flags:                             0x0
  Size of this header:               64 (bytes)
  Size of program headers:           56 (bytes)
  Number of program headers:         11
  Size of section headers:           64 (bytes)
  Number of section headers:         29
  Section header string table index: 28
```
- `Entry point address: 0x0`ここがおかしい(普通は0ではなく、なんらかの値になる)
- entrypointは通常、`endbr64`や`xor    ebp,ebp`が書かれているので、それを探す
```
$ objdump -d -M intel mitsu_200 | grep "endbr64"
$ objdump -d -M intel mitsu_200 | grep "xor"
    1044:       31 ed                   xor    ebp,ebp
    115a:       83 f0 39                xor    eax,0x39
    11c8:       31 db                   xor    ebx,ebx
```
- 1044に`xor ebp, ebp`があるので、entry pointは1040であることがわかる。
- ELFの規格で、ヘッダのoffset 0x18に1040を書き込めばよい(エンディアンに注意して、4010と書き込む)
- radare2を使う
```
$ r2 -w mitsu_200
> aaaa
> s 0x00000000
> wx 4010 @ 0x18
```
- これでOK。実行すると
```
$ ./mitsu_200
You could execute this binary! hai pro.
```
- breakpointを適当に仕掛けてメモリの中をのぞくとフラッグもとれる。


### G. packman
- まず、`radare2`で見てやるとfcn....がたくさんあって気が滅入るので、基本的なstringsで調べてみます。
```
$ strings packman
...
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 3.94 Copyright (C) 1996-2017 the UPX Team. All Rights Reserved. $
_j<X
...
```
- upxをググります。どうやら圧縮・解凍を行うソフトのようです。
- upxをダウンロードしてpackmanを解凍します。
- 解凍後のファイルを再びradare2にかけると中身が見えます
- Do you know ROT?という文字列と、怪しい文字列`txpgs{V_nz_CNPXZNA}`が見えます。
- 怪しい文字列をROT13にかけて、`gkctf{I_am_PACKMAN}` -> AC
- 出典: mitsuさんの自作問題