# scs7
```
nc crypto.chal.ctf.westerns.tokyo 14791
Note: "You can encrypt up to 100 messages" は一回の接続中での制限を意味します。
```

# do
- 接続してみる
```
encrypted flag: Jda1Kekovs9TEbMMULh3DMeEP7uR68UkkWYb1iEXBxrzrcP8VFd3FatzBgXUrFpM
You can encrypt up to 100 messages.
message:
```
- `Jda1Kekovs9TEbMMULh3DMeEP7uR68UkkWYb1iEXBxrzrcP8VFd3FatzBgXUrFpM`
- 長さは64
- 適当にmessage打ち込む
```
encrypted flag: qjpbSY2CaRX1mnQQ3gTDsQYmc6t0ok322NJnbGmHiLuwuAckP8jD8pVwi4H3u8ZQ
You can encrypt up to 100 messages.
message: aaa
ciphertext: YnmB
message: aaa
ciphertext: YnmB
message: aaa
ciphertext: YnmB
message: bbb
ciphertext: YWAb
message: bbb
ciphertext: YWAb
message: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ciphertext: LkCk61edLjfpDaxACtUbS3Qk8fdY2Nz3Lk6VCfUbG1EavrJRBe1f8
message: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ciphertext: FqcnaLeZgjArxwuDzHBnsfv7ZB9A6ZJhggW6J1nm5Hk74DaZghzPLiYZaW1RhwYaeF3cxuC1tzqjAN79cihkhBbtFSKGFiMp97PWEVVTRPWs6d7BbYp9wEiGyhMfNeVipF177JgxE8Ys
message: s^H^H
ciphertext: tweF
message: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
ciphertext: pkudFXPTFpYMZfcoZ9otkrzRzG0p9wYtftFZcgbfVPNB
```
- messageに応じてencryptしてくれていて、長さによって変化するらしい。
- 1文字か2文字ずつ増えていく…？文字種によらない
- 64の長さになるものを探す→毎回内容が変わるので、64の長さは変化しないけど100回のうちに当てる必要がある
- でも長さ決め打ちしてもbrute-forceできない長さだぞ…？分からない

# 解説見た
- [brute-force-attackする手法](https://hiziriai.hatenablog.com/entry/2018/09/03/101748) と [Base59と見抜く手法](https://qiita.com/kusano_k/items/9731a60a13273b320dea#scs7-warmup-crypto) の二つがある
- ここではBase59と見抜く手法でやる。
- 通信を自動化する必要はなくて([通信を自動化したもの](https://github.com/p4-team/ctf/tree/master/2018-09-01-tokyowesterns/crypto_scs7)もある)、いくつか入れてから手元で回せばOK
#### まずどうやってBase59と気づくか？
```
message: aaa
ciphertext: YnmB
message: aaa
ciphertext: YnmB
message: aaa
ciphertext: YnmB
```
- ここと、nc接続するたびに変化するところから毎回規則は変わってて、接続したときの規則は同じことが分かる。
- あとは文字の長さに依存すること、登場する文字が`a-z,A-Z,0-9`(62文字)から`IOl`を除いた59文字と分かる。(bitcoinアドレスなどで用いられるbase58はさらに`0`を除いていて、この形式を知っていたら思いついたかもしれない、あとbase64を見慣れていたらbaseXXだと気づけたかもしれない)

#### encode, decode
```
message: a
ciphertext: qE
message: b
ciphertext: qj
message: c
ciphertext: qo
message: d
ciphertext: qu
message: e
ciphertext: q2
message: f
ciphertext: qV
message: g
ciphertext: qg
message: h
ciphertext: qy
```
- ここからbase58のencodeを行う
- [Javaでbase58](http://java-lang-programming.com/ja/articles/23)の記事を見て、baseXXのアルゴリズムを確認
    - 文字列を16進数に変換
    - 16進数を10進数に変換
    - 10進数を58進数に変換(あまりから文字を決定してくっつけて58で割る→最後に文字列を逆順にする)
- baseってよく考えたら底みたいな意味だったわ、これXX進数ってことか...
- use_charの順列が毎回変わっているので、58種類の出力を得て対応表を作る
- encoded_flagを対応表を用いて0123...のuse_charに直す
- そのuse_charをdecode→flagを得る、という流れ
- おおお理解
```
b'A'
N89YzHL0NVG6558zLtmeMrnCzCGXsbDT15hHDN0o7QSKdLRTfXm3QL7huc3CdgLgPvxN
Tjkv5wGzTRiJWWj5GaQ4e7A959icX1sFtWfwsTzmgLKYEGPFycQdLGgfUpd9EVGVD2qT
NMd1hF50NixQPNqqDBxTCLtmxz1VmRrhGvQgWXyN3qdYbuUmb4iUNmGJ0ddv7ewZWsFb
TeEtfZWzTBqLDTMMsrqF9GaQq5tRQP7fi2LVHcNTdMEv1UhQ1oBhTQiuzEE2g4xbHXZ1
Nb5VQCq0NxdihgXg5W8G2r0KwkmTfGUwYk84ohvx0FpmaTY4WcfuMBQu6fDccdXSdoZp
T1WRL9MzTqEBfVcVWHji87zYxSQFyihxvSjomf2qzZ3QnFvoHpyUerLUJysppEcKEmb3
NpYy7Aa0PBK20zDWxpK4tL6tvXWRZ77ApZrU5stWwh0zZ1bNS9dKKcZVCgpK6c7Kkjt2
T3vNg0nzDrY8z5sHq3YoaGJa2cHPbgg03b7hWXaHxfz5bt1TKkEYYpbR9V3YJpgYSCa8
{'0': 'A', 'b': 'Z', '4': 'e', 'z': '0', 'W': '5', 'V': 'g', 'x': 'w', 'Q': 'm', 'd': '3', 'v': 'Y', 'E': 'd', 'T': 'N', 'R': 'V', 'N': 'y', '7': 'r', 'n': 'a', 'K': 'S', 'M': 'q', 'J': '6', '5': 'z', 'r': 'B', 'o': '4', 'U': 'u', 'g': '7', '2': 'v', 'y': 'f', 'p': 'c', '1': 'b', 'D': 'P', 'A': 'n', 'H': 'W', 'h': 'U', 's': 'D', 'G': 'L', 'B': 'i', 'Z': 'F', 'w': 'H', 'C': 'j', 'i': 'G', 'L': 'Q', '9': 'C', 'a': 't', 'k': '9', 'S': 'k', '3': 'p', 'j': '8', 'X': 's', 'u': 'J', 'F': 'T', 'f': 'h', '8': '2', 'e': 'M', 'q': 'x', 'c': 'X', 'Y': 'K', 'm': 'o', 't': '1', 'P': 'R'}
s7dwvcRrt10Jeo229BqE32ceU5pGaj9RRYCowVeTiKLfLZUjuQ7EQdAfiST9LQN2
Dr3HYXVB1bA6M4vvCixdpvXMuzcLt8CVVKj4HgMNGSQhQFu8Jmrdm3nhGkNCQmyv
b'TWCTF{67ced5346146c105075443add26fd7efd72763dd}'
```
- 対応表があり、与えられた文字列でs→use_charでDという風に対応している。
- 最後から三行目がciphertextで、最後から2行目がuse_charへの変換、それをdecodeしたものが最後の行。
- `TWCTF{67ced5346146c105075443add26fd7efd72763dd}` -> AC

# 感想
- 最後hexにしてて詰まった。hex2asciiをする必要があった(でないとTWCTFの文字が出てこない)
