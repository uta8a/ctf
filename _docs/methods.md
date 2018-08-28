# CTFを解くための手段
- 積み残し
- ksnctf 4,6
- picoctf
- tjctf Bricked Binary, Future Canary Lab, Math Whiz, Mirror Mirror, Online Banking, Secret Secrets, Tilted Troop [Pwn系]
- +問題例はex.をつけて自分のGitHubへのリンクを貼る(リンク先がなくなる恐れがあるため)

## common
- file
- strings: gifとかの画像などにも有効(`grep 'flag{'`が役立つ)
- grep
- brute-force-attack(ものすごい多岐にわたる)
- nc 000.0.00.000
- nmap: 空いているポート番号を調べる
- curl
    - install: `sudo apt install curl`
- tar.gzの解凍方法→`tar -zxvf file.tar.gz`


## Crypto
- Caesar(ROT)
- sha1: [hashtoolkit](http://hashtoolkit.com/)
- CRT [CRT tool](https://www.dcode.fr/chinese-remainder)
- RSA [参考資料](https://www.slideshare.net/sonickun/rsa-n-ssmjp)
    - common modulus attack: m,n共通、eが異なる場合
    - Fermat: p,qが近い場合: [ex. Classic](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Classic/14.md)
- base64
    - `cat file.txt |tr -d '\n' | base64 -d`
- 鍵の長さを先に求めてからbrute-force-attack: [ex. Bad Cipher](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Bad_Cipher/1.md)
- wordsearch 縦横に読むことで意味のある単語を探し出す手法: [word-search](https://github.com/robbiebarrat/word-search)→まだライブラリ化できてない(右上を取得していくスクリプトみたいな): [ex. Caesar's Compilation](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Caesars_Complication/9.md)
- md5: [md5 decrypter](http://hashtoolkit.com/decrypt-md5-hash/)
- LC4: [tool](https://github.com/dstein64/LC4)
- [Cayley-Purser Algorithm](http://www.tbasic.org/reference/old/cp.pdf) Sarahという女の子が開発した暗号方式。当時はRSAを超えるのではと期待されたが、実際は脆弱性があった。[復号方法](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Sarahs_Cryptosystem/1.md)
- Latencyとbrute-force-attackを利用した統計的な攻撃: [ex. Speedy Security](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Speedy_Security/1.md)
- Vigenere暗号(鍵の繰り返しがあるので、与えられるものは鍵の長さということがある。brute-force-attackして意味のある文字列を出すというのも有効。)


## Web
- htmlのソースコードを読む
- cookieを見る: 保護された通信 > Cookie
- devtools
    - header(meta)
    - network: Preserve log(X-flag)
- SQLinjection
    - `SELECT * FROM table`
    - `' OR 'A'='A' --`
    - table名のエスパー`ip_address`など
- pythonでフォームに送るのを自動化→[ex. code](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Ess_Kyoo_Ell/sub.py)
- brute-force
    - こういうものはpythonで自動化する
        - [ex. Moar Horses [code]](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Moar_Horses/solve.py)
- directory系のもの
    - `a://file.php`のようにファイルに直接アクセスできる形のときはディレクトリを利用できる。
        - rootに飛び、`/proc/self/cwd`で現在動いているプログラムのディレクトリに飛べる [ex. Programmable Hyperlinked Pasta](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Programmable_Hyperlinked_Pasta/1.md)
- curl
    - GET/PUT/POST/DELETEをオプションで使える[ex. [code]](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Request_Me/solve.py)


## Pwn
- Exploit codeを書くものをPwn, そうでないものをREという分類をしています。



## RE
- objdump
    - `objdump -s file`
- radare2
    - `r2 -d file` debugモード
    - `aaaa`
    - `s main`
    - `pdf`
    - `pdd`
    - `db address` addressにブレークポイント設置
    - `pxr @ esp` メモリの値を見る
- pddでコード読んで、それをpythonに移植してflagを得る手法
- ブレークポイントを設置して、実行後のメモリの値を見る手法
- python
    - encrypt programが与えられているとき
    - とりあえず`ctf{`などを入れてencryptしたものと、decryptしたいものを見比べる→brute-force-attack
- ltraceをかけて実行`ltrace ./file`
    - strlenで長さ確かめ→strcmpでflag確認というステップを踏んでる場合、長さを特定すればltrace時にflagがわかる。[ex. Validator](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Validator/13.md)

## Network
- tcpdump
    - `tcpdump -qns 0 -A -r file.pcap`
- wireshark
    - Export Objects -> http
    - Export ASCII flag.jpg
    - FTPデータからのzip取り出し
    - key.pemを使ったSSLの読み取り
        - `Preferences > SSL > Edit`
        - 
- ftpコマンド
    - `ftp 000.0.00.000`で接続
    - `ls -al`
    - `get file`でダウンロード


## Forensics
- Exif: latitude,longitude→[maps](http://earthjp.net/maps/)
- morse code [English Translator](http://morse.ariafloat.com/en/)
- file
    - OpenDocumentFormat,odg(zip)
    - Microsoft OOXML(Excel)
    - Hierarchical Data Format (version 5) data(mdf5): 機械学習のモデルのファイル: [ex. Learn My Flag](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Learn_My_Flag/11.md)
    - jpg バイナリの開始は`FFD8`(なので、見れないときは`vim -b flag.jpg`としてFFD8より前を削除するとよい)
- png内のファイル取り出し: `binwalk file.png`
    - install: `sudo apt install binwalk`
- zipのパスクラック(長さ2のパスワードをbrute-force-attack)→ `fcrackzip --brute-force --charset a1 --length 1-3 --use-unzip file.zip` 
    - install: `sudo apt install fcrackzip`
- 画像ファイルを開くとき→`eog file.png`
- ImageMagick: `compare file1.png file2.png diff.png`で二つの画像のdiffがとれる
- GIMP: threshold(閾値)を変化させると文字が浮かび上がる→スラッシュでコマンド呼び出し、thresholdと打ち込む
- QRコード読み込み: スマホで行う。QRコードを黒にするため白黒反転を使うことがある
- GIMP: 白黒反転→スラッシュでコマンド呼び出し、invertで白黒反転
- QRコード、一部が破損: [decoder](https://github.com/waidotto/strong-qr-decoder/)
- LSB(least significant bit)を調べる問題 : [tool](https://github.com/zed-0xff/zsteg) MSBとかも調べられる
    - install: `sudo gem install zsteg`
- RGBなどをいい感じに変化させてくれるもの(あまり原理は分かってない) [stegsolve](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve) `java -jar stegsolve.jar`で起動


## Misc
- js難読化: nodejsでローカル実行してエラー情報を見る(ソースコードが読める): [ex. unya.js](https://github.com/tMasaaa/ctf/blob/master/ksnctf/3/unya.js)
- gitプロトコル: ネットワークプロトコルは4つある。nmapで9418が開いている場合、[Gitプロトコル](https://git-scm.com/book/ja/v1/Git-%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC-%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB)を疑う
- git cloneで一部のみ取り出す`git clone --depth=1 git://000.000.000.000/xxx`で深さ1の部分を取ってこれる
- pyjail
    - [ex. Mirror Mirror](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Mirror_Mirror/1.md)
    - [ex. The Abyss](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/The_Abyss/1.md)
- 10進数→16進数→ASCII(decode hex)という変換で意味のある内容になるもの。使われている数字や文字から何進数なのか考える。[ex. [code]](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Nothing_but_Everything/a.py)