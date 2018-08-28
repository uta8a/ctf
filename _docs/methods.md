# CTFを解くための手段
- 積み残し
- ksnctf 4,6
- picoctf
- tjctf Bricked Binary, Future Canary Lab, Math Whiz, Mirror Mirror, 
- +問題例はex.をつけてGitHubへのリンクを貼る(リンク先がなくなる恐れがあるため)
- Online Bankingからやる。

## common
- file
- strings
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
- RSA
    - common modulus attack: m,n共通、eが異なる場合
    - Fermat: p,qが近い場合: [ex. Classic](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Classic/14.md)
- [RSA参考資料](https://www.slideshare.net/sonickun/rsa-n-ssmjp)
- base64
    - `cat file.txt |tr -d '\n' | base64 -d`
- 鍵の長さを先に求めてからbrute-force-attack: [ex. Bad Cipher](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Bad_Cipher/1.md)
- wordsearch 縦横に読むことで意味のある単語を探し出す手法: [word-search](https://github.com/robbiebarrat/word-search)→まだライブラリ化できてない(右上を取得していくスクリプトみたいな): [ex. Caesar's Compilation](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Caesars_Complication/9.md)
- md5: [md5 decrypter](http://hashtoolkit.com/decrypt-md5-hash/)



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


## Pwn



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


## Network
- tcpdump
    - `tcpdump -qns 0 -A -r file.pcap`
- wireshark
    - Export Objects -> http
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
- 


## misc
- js難読化: nodejsでローカル実行してエラー情報を見る(ソースコードが読める): [ex. unya.js](https://github.com/tMasaaa/ctf/blob/master/ksnctf/3/unya.js)
- gitプロトコル: ネットワークプロトコルは4つある。nmapで9418が開いている場合、[Gitプロトコル](https://git-scm.com/book/ja/v1/Git-%E3%82%B5%E3%83%BC%E3%83%90%E3%83%BC-%E3%83%97%E3%83%AD%E3%83%88%E3%82%B3%E3%83%AB)を疑う
- git cloneで一部のみ取り出す`git clone --depth=1 git://000.000.000.000/xxx`で深さ1の部分を取ってこれる
- pyjail
    - [ex. Mirror Mirror](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Mirror_Mirror/1.md)
    - [ex. ]()
- 10進数→16進数→ASCII(decode hex)という変換で意味のある内容になるもの。使われている数字や文字から何進数なのか考える。[ex. [code]](https://github.com/tMasaaa/ctf/blob/master/tjctf2018/Nothing_but_Everything/a.py)