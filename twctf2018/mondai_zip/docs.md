# mondai.zip
```
mondai.zip
```

# do
- おそらくcapture.pcapngからpasswordを復元する問題
- ubuntuでやる。
- pcapngファイルを見たけど分からない。ICMPというものらしいけど、abc...が並んでいるだけで何も見えてこない

# 解説見た
- [kusanoさんのWriteup](https://qiita.com/kusano_k/items/9731a60a13273b320dea#mondaizip-warmup-misc)を参考に
- まず、pcapngとは？
    - pcapより新しいファイルフォーマット。pcapとは構造が異なる。(pcapは2つのヘッダ、それに対しpcapngは様々なブロックで管理されている)
    - pcapngは複数インターフェースをサポート
    - [ここ](http://slankdev.hatenablog.com/entry/2015/12/22/000000)に構造の違いが説明されている
    - 調べてもpcapngはあまり歓迎されてないっぽくて、pcapへの変換方法ばかり出てくる
#### 1段階目
- 最初の`y0k0s0.zip`は適当に`y0k0s0`とか打つと開ける。(ここは人力でやったけど、JohnTheRipperを使ってもいける)

#### 2段階目
- Wiresharkを使ってabc...が怪しいなというところまで来ていたのでそこを抜き出す
- 1つ目の往復(めんどくさかったのでradare2で見ています)
```
0x00000170  0b03 c0a8 0b05 0800 65f0 0001 01f3 6162  ........e.....ab
0x00000180  6364 6566 6768 696a 6b6c 6d6e 6f70 7172  cdefghijklmnopqr
0x00000190  7374 7576 7761 6263 6465 6667 6869 6a6b  stuvwabcdefghijk
0x000001a0  6c6d 6e6f 7071 7273 7475 7677 6162 6364  lmnopqrstuvwabcd
0x000001b0  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
0x000001c0  7576 7761 6263 6465 6667 6869 6a6b 6c6d  uvwabcdefghijklm
0x000001d0  6e6f 7071 7200 0000 a400 0000 0600 0000  nopqr...........
```
- 2つ目の往復
```
0x000002c0  7ff9 0001 01f4 6162 6364 6566 6768 696a  ......abcdefghij
0x000002d0  6b6c 6d6e 6f70 7172 7374 7576 7761 6263  klmnopqrstuvwabc
0x000002e0  6465 6667 6869 6a6b 6c6d 6e6f 7071 7273  defghijklmnopqrs
0x000002f0  7475 7677 6162 6364 6566 6768 696a 6b6c  tuvwabcdefghijkl
0x00000300  6d6e 6f70 7172 7374 7576 7761 6263 6465  mnopqrstuvwabcde
0x00000310  6667 6869 6a6b 6c6d 6e6f 7071 7273 7475  fghijklmnopqrstu
0x00000320  7677 6162 6364 6566 6768 6900 b000 0000  vwabcdefghi.....
```
- 3つ目の往復
```
0x00000420  73e9 0001 01f5 6162 6364 6566 6768 696a  s.....abcdefghij
0x00000430  6b6c 6d6e 6f70 7172 7374 7576 7761 6263  klmnopqrstuvwabc
0x00000440  6465 6667 6869 6a6b 6c6d 6e6f 7071 7273  defghijklmnopqrs
0x00000450  7475 7677 6162 6300 7c00 0000 0600 0000  tuvwabc.|.......
```
- 4つ目の往復
```
0x00000510  0b03 c0a8 0b05 0800 e95f 0001 01f6 6162  ........._....ab
0x00000520  6364 6566 6768 696a 6b6c 6d6e 6f70 7172  cdefghijklmnopqr
0x00000530  7374 7576 7761 6263 6465 6667 6869 6a6b  stuvwabcdefghijk
0x00000540  6c6d 6e6f 7071 7273 7475 7677 6162 6364  lmnopqrstuvwabcd
0x00000550  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
0x00000560  7576 7761 6263 6465 6667 6869 6a6b 6c6d  uvwabcdefghijklm
0x00000570  6e6f 7071 7273 7475 7677 6162 6364 6566  nopqrstuvwabcdef
0x00000580  6700 0000 b000 0000 0600 0000 b000 0000  g...............
```
- 5つ目の往復
```
0x00000670  0b03 c0a8 0b05 0800 52ce 0001 01f7 6162  ........R.....ab
0x00000680  6364 6566 6768 696a 6b6c 6d6e 6f70 7172  cdefghijklmnopqr
0x00000690  7374 7576 7761 6263 6465 6667 6869 6a6b  stuvwabcdefghijk
0x000006a0  6c6d 6e6f 7071 7273 7475 7677 6162 6364  lmnopqrstuvwabcd
0x000006b0  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
0x000006c0  7576 7761 6263 6465 6667 6869 6a6b 6c6d  uvwabcdefghijklm
0x000006d0  6e6f 7071 7273 7475 7677 6162 6364 6566  nopqrstuvwabcdef
0x000006e0  6768 696a 6b6c 6d6e 6f70 7172 7300 0000  ghijklmnopqrs...
```
- 6つ目の往復
```
0x000007f0  c63f 0001 01f8 6162 6364 6566 6768 696a  .?....abcdefghij
0x00000800  6b6c 6d6e 6f70 7172 7374 7576 7761 6263  klmnopqrstuvwabc
0x00000810  6465 6667 6869 6a6b 6c6d 6e6f 7071 7273  defghijklmnopqrs
0x00000820  7475 7677 6162 6364 6566 6768 696a 6b6c  tuvwabcdefghijkl
0x00000830  6d6e 6f70 7172 7374 7576 7761 6263 6465  mnopqrstuvwabcde
0x00000840  6667 6869 6a6b 6c6d 6e6f 7071 7273 7475  fghijklmnopqrstu
0x00000850  7677 6162 6364 6566 6768 696a 6b6c 6d6e  vwabcdefghijklmn
0x00000860  6f70 7100 b800 0000 0600 0000 b800 0000  opq.............
```
- 7つ目の往復
```
0x00000bd0  0b05 0800 7ff1 0001 01fc 6162 6364 6566  ..........abcdef
0x00000be0  6768 696a 6b6c 6d6e 6f70 7172 7374 7576  ghijklmnopqrstuv
0x00000bf0  7761 6263 6465 6667 6869 6a6b 6c6d 6e6f  wabcdefghijklmno
0x00000c00  7071 7273 7475 7677 6162 6364 6566 6768  pqrstuvwabcdefgh
0x00000c10  696a 6b6c 6d6e 6f70 7172 7374 7576 7761  ijklmnopqrstuvwa
0x00000c20  6263 6465 6667 6869 6a6b 6c6d 6e6f 7071  bcdefghijklmnopq
0x00000c30  7273 7475 7677 6162 6364 6566 6768 6900  rstuvwabcdefghi.
```
- 並べると、
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqr
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghi
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabc
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefg
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrs
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopq
- abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghi
- 同じ文字の繰り返しで、こういうときは(tjctfのVigenere暗号のキーでもあったけど)長さに注目するのが典型っぽい。
- 長さをASCIIに変換する。
```
>>> a = ["abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqr", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghi", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabc", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefg", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrs", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopq", "abcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghijklmnopqrstuvwabcdefghi"]
>>> for i in a:
...     print(chr(len(i)))
...
W
e
1
c
o
m
e
```
- `We1come`と出てきたのでそれをmondai.zipに適用→list.txtが出てくる

#### 3段階目(stage2)
- list.txtの中を試す→`stage2/solve.py`(solve.pyを動かすと、1c9ed78bab3f2d33140cbce7ea223894という名前のEmptyなファイルが出てくるので、password`eVjbtTpvkU`を表示させて普通にGUIで打ち込んだら、1c9ed78bab3f2d33140cbce7ea223894という名前のzipファイルが出てきた)
- `1c9ed78bab3f2d33140cbce7ea223894`というファイルが出てくる。

#### 4段階目(stage2)
- hashのように見えるので[ここ](http://hashtoolkit.com/reverse-hash/?hash=1c9ed78bab3f2d33140cbce7ea223894)で複数のハッシュチェックを一気にできるのでかけてみるとmd5で`happyhappyhappy`と分かる。
- ubuntuのGUI Extract Managerで`1c9ed78bab3f2d33140cbce7ea223894`に対して`happyhappyhappy`を適用

#### 5段階目(stage3)
- READMEには`password is too short`とあるのでfcrackzipを使う。
- `fcrackzip --brute-force --charset a1 --length 1-5 --use-unzip mondai.zip`2~4文字でbrute-force
- `to`がパスワードだとわかったのでまたGUIで打ち込んで開く

#### 6段階目(stage4)
- secret.txt
```
Congratulation!
You got my secret!

Please replace as follows:
(1) = first password
(2) = second password
(3) = third password
...

TWCTF{(2)_(5)_(1)_(4)_(3)}
```
- X段階目を思い出す。順に、
- `y0k0s0`
- `We1come`
- `eVjbtTpvkU`
- `happyhappyhappy`
- `to`
- だったので、`TWCTF{We1come_to_y0k0s0_happyhappyhappy_eVjbtTpvkU}` ->AC




