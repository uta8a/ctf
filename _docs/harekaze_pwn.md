# pwn予習
- pwnの最終目標はシェルをとること
# レジスタとは
    - 実行速度最速、プロセッサ内蔵の記憶回路
    - レジスタでどう計算をやりくりするか→コンパイラ最適化のテーマ、レジスタ割り付け

| 32bit | 64bit | 備考 |
|:----|:----|:----|
| eax | rax | 汎用レジスタ |
| ecx | rcx | 汎用レジスタ |
| edx | rdx | 汎用レジスタ |
| ebx | rbx | 汎用レジスタ |
| esp | rsp | スタックポインタ |
| r8d | r8 | 拡張汎用レジスタ |

- r8~r15のレジスタが拡張されている
- espはradare2で見ると嬉しいとこ(スタック)

# AMD64とは
- 呼び方の問題。

| 呼び方 | 説明 |
|:----|:----|
| AMD64 | x86を64ビットに拡張したアーキテクチャ。AMD命名 |
| IA-32e | IA-32の64ビット拡張。 |
| EM64-T | Extend Memory 64 Technology の略。意味はIA-32eと同じ |
| x86-64 | x86を64ビット拡張しましたよ、という意味 |
| x64 | 総称 |

> x86を64ビット拡張とはどういうことなのか？
> →アーキテクチャでの相違点を考える
- x86は32ビットだった→AMD64では64ビットに拡張
    - ひとつのレジスタで表現できるアドレス空間が、理論上4GB -> 16EB に拡張
- 汎用レジスタが8本→16本に増えた
    - メモリアクセスを少なくして、レジスタのみで処理をパスすることがアセンブラ使いやコンパイラ開発者にとって重要なので、これは恩恵が大きい
- SSE2: 実数計算が速くなった(よくわからない)

# システムコール
- システムコール: プログラムがカーネルにアクセスしてタスクを実行する方法のこと。
- [ここ](http://man7.org/linux/man-pages/man2/syscalls.2.html)に一覧がある
- glibcはラッパー
> カーネルになんでアクセスする必要があるのか？
> ユーザープログラムが入出力を行えばいいじゃん
- 特権レベルという概念がある。
- カーネルは特権レベルがRing0(最高)、ユーザープログラムはRing3で実行される

# 特権レベルとは
- カーネルモード(無制限のCPU動作ができる状態)では、具体的には任意の命令を実行でき、入出力操作を開始でき、全メモリ空間にアクセス可能
- 複数の特権レベルを持ったコンピュータアーキテクチャの一種にリングプロテクションがある。
> なんで特権レベルを分けるのか？→保護のため
- フォールトトレラント性(データ、機能を障害から保護する)、コンピュータセキュリティ(悪意ある行為からの保護)が目的


# 気づき
- 抽象化がポイント。
> 例えば、キーボードは各社いろいろあるけど、入力として受け取るときには各社の仕様に精通してないと取り扱えないみたいなことが起きると困る。ある程度抽象化されていて、プログラム上ではそういうデバイスの違いに悩まされないようになっていると嬉しい

# 参考
- https://codezine.jp/article/detail/457 AMD64
- https://postd.cc/the-definitive-guide-to-linux-system-calls/ システムコール
- http://man7.org/linux/man-pages/man2/execve.2.html execveについてのman
- https://ja.wikipedia.org/wiki/CPU%E3%83%A2%E3%83%BC%E3%83%89 CPUモード
- http://blog.livedoor.jp/sonots/archives/18193659.html システムコールの統計情報、straceの使い方(チューニング、システムコールが呼ばれた回数の表示など)
- https://qiita.com/h2suzuki/items/c2b0b51abb252155db2f システムコール番号を探す
- http://inaz2.hatenablog.com/entry/2014/07/04/001851 スタックバッファオーバーフローの実演