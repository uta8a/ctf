# FormatStringAttack
- sample
- fgets
```
#include <stdio.h>
char *fgets(
    char * restrict s,
    int n,
    FILE * restrict stream
);
```
- 3つ引数をとる。
    - ひとつめ: 格納する配列
    - ふたつめ: 最大文字数はn-1(null文字が最後に入る)
    - みっつめ: ストリーム(データの流れ 入力、出力)
- ストリームについて
- https://programming-place.net/ProgrammingPlacePlus/c/043.html
- バッファリング: データをいったんどこかに蓄えておいて、あるタイミングで処理する方法のこと。
- バッファ: 蓄えておく場所のこと。


- stdin(標準入力)standard input
```
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
- http://milkpot.sakura.ne.jp/note/x86.html
- x86のアセンブラ
- eip/ripはプログラムカウンタ(32bit, 64bit)
- プログラムカウンタ: 次に実行する命令のメモリ番地を管理するレジスタ。PCと略されることも。CPUは次に実行する命令が格納されているPCから読み出し、順次実行する。
- PCに0x8020が格納されている→今CPUが実行しているのは0x8019番地の命令
- プロセッサはメモリ上に保存されたプログラムの実行位置を記憶している。(CPUはプロセッサの一種)
- https://toshiba.semicon-storage.com/jp/design-support/e-learning/micro_intro/chap4/1274772.html
- つまり、"私はpwnをする上で一番重要なことは任意のメモリへの書き込みだと考えている. プログラムの制御を奪うためには何らかの方法でEIP(RIP)を書き換えなければならないが, 一般的にx86(x64)ではプログラムの格納されているアドレスをメモリに配置しているため, 任意のアドレスを書き換えることでその制御を奪うことができるようになるのだ"を分かりやすくすると、"任意のメモリへの書き込みが大事→eip/ripの書き換えは次にCPUが実行する命令のアドレスを指定することにつながる。命令の格納されているアドレスがメモリに置いてあるので、メモリの書き換えがそのまま制御を奪うことにつながる。"