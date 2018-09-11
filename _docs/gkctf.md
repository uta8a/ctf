# 環境構築について
- 基本的にはbinary問を解くときはlinuxでの実行可能ファイルが渡されます(ELFと呼ばれます)
    - だんだん進んでいくとwindowsでの実行可能ファイル(dllと呼ばれます)が出題されることもありますが、ここでは扱いません。

## linuxの環境を作る
- windowsの上にlinux環境を作る感じで話を進めていきます。適当に読み替えたり読み飛ばしたりしてください。
- VirtualBoxをインストールします。
- ubuntu16.04を入れます(18でもOKです)
    - このあたりは[VirtualBox ubuntu]などの検索ワードでQiitaなどを見るのが早いです。
- 基本的に、CUIを使うのでvagrantfileを作成してコマンドプロンプトからubuntuに接続できるようにします。(これはそうすると楽なだけで、もちろんvirtualboxそのままを使ってもOKです)
    - これも適当にググりましょう
- これでlinuxの環境が構築できました(ほとんどググるしか言ってない気がする)

## radare2を使う
- radare2はバイナリ解析ツールです。
    - objdump+gdbという方法もありますが、今回は僕が少し慣れているという理由でradare2を紹介しています。
- インストールについて
    - aptで入れるのは古いので、githubから落としてくることが推奨されています。
- `git clone https://github.com/radare/radare2.git`: githubからリポジトリを落としてくる
- `cd radare2`: radare2ディレクトリに移動
- `sudo ./sys/install.sh`: インストールシェルの実行
- これでradare2が入ります。確認として、バイナリファイル`binary_file`に対して、`r2 binary_file`とするとなにか動くはずです

<br>

- `r2 file`でradare2でバイナリを開きます。
## よく使うコマンド
- `aaaa`: これは初手必ず行う感じの、おまじないです
- `afl`: analysis function list関数一覧を呼び出します。怪しい関数`secret.func`があれば、`s secret.func`で飛んで`pdf`すれば中身がディスアセンブルされたものが見れます
- `s main`: main関数に飛びます
- `pdf`: バイナリがディスアセンブルされたものが表示されます。
- `db [address]`: addressにブレークポイントを仕掛けます
- `dc`: ブレークポイントまで実行します
- `pxr @ [address]`: addressからのメモリの値を表示します。addressにはrsp, espなどのスタックポインタを指定すると嬉しいことが多いです。

## その他[radare2とは関係ない]
- もっと多くの情報を表示させながらバイナリを実行したい場合は、`ltrace ./file`とするとよいです。