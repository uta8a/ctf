# CTFを解くための手段
- 積み残し
- ksnctf 4,6
- picoctf
- tjctf
## common
- file
- strings
- grep
## Crypto
- Caesar(ROT)
- sha1: [hashtoolkit](http://hashtoolkit.com/)
- CRT [CRT tool](https://www.dcode.fr/chinese-remainder)
- RSA
    - common modulus attack: m,n共通、eが異なる場合
- [RSA参考資料](https://www.slideshare.net/sonickun/rsa-n-ssmjp)
- base64
    - `cat file.txt |tr -d '\n' | base64 -d`
## Web
- devtools
    - header(meta)
    - network: Preserve log(X-flag)
- SQLinjection
    - `SELECT * FROM table`
    - `' OR 'A'='A' --`
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
- opendocumentformat,odg(zip)

## misc
- js難読化: nodejsでローカル実行してエラー情報を見る(ソースコードが読める)
- 