# Revolutional Secure Angou
```
revolutional-secure-angou.7z
```

# 解説見た
- [kusanoさんのwriteup](https://qiita.com/kusano_k/items/9731a60a13273b320dea#revolutional-secure-angou-crypto)を参考にした
- [これ](https://www.xmisao.com/2014/09/25/debian-linux-extract-7z.html)を見てp7zip-fullを入れた`sudo apt install p7zip-full`
- `7z x revolutional-secure-angou-de97106aa248a41a40fdd001fc5f7b4b4f28a39eb6bcabf8401b108b7a8961c5.7z`で解凍
- 中身を順にみていく
```
vagrant@vagrant:~/working/rsa/revolutional-secure-angou$ cat flag.encrypted
O�7ry�.H��_�W-�]/�j|�   7����O�l�м�
�3�0B������ad�Smqc�����V<�}��|��0�o��ǔ���0����>����#�Bs-�&Fҩ�&B�Q(��\jK�[>#"�z�=�  ���W<��yt���    Û�P���ٞ�=�P���ӷ���u�)�jd�ʵ���q0k�XAvkWnG'��TƎB����W��
```
```
vagrant@vagrant:~/working/rsa/revolutional-secure-angou$ cat publickey.pem
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhSkGPqCtO0Ypb5L3I1Z3
LqTnA/e3kiDBjeG348oKdyjRnmncSLhoXNYE9Yh6T486lFocoVk88IbTSOxNySFC
CD/J4iA8ZTAxHuUQvlCkKu5KY+f6Zr/ONRL8L7EXQCpVzfCJd3DBu4by2TBtpbiZ
0pTtvLF62H4XWSzMP2KxMFckGBcyrHR0zyO+tyKDM3PvB7apIYjPKLz+8msjaK2j
j39P2JIdvjtkiOS5ICj/vUauJti0PJqG27xj8LUTmLtUCY/3AEtkavtC8kNUq2ot
MO/u6LMzRzq+HMkutopGWBnZ6aD/WP6vLHIq5lt87cnjC+kVAp1pNCUjuYGtg5XN
9wIDAQAB
-----END PUBLIC KEY-----
```
```
vagrant@vagrant:~/working/rsa/revolutional-secure-angou$ cat generator.rb
require 'openssl'

e = 65537
while true
  p = OpenSSL::BN.generate_prime(1024, false)
  q = OpenSSL::BN.new(e).mod_inverse(p)
  next unless q.prime?
  key = OpenSSL::PKey::RSA.new
  key.set_key(p.to_i * q.to_i, e, nil)
  File.write('publickey.pem', key.to_pem)
  File.binwrite('flag.encrypted', key.public_encrypt(File.binread('flag')))
  break
end
```
- RSA風のなにかを作っているみたい。
- Ruby分からないので[このへん](https://docs.ruby-lang.org/ja/latest/class/OpenSSL=3a=3aBN.html)を見ていく
- pは1024bitで真に安全でない素数((p-1)/2が素数とは限らないもの)
- mod_inverseは逆元を返すので、new(e).mod_inverse(p)で`mod p`における`e`の逆元ということになる
- それでqが素数の場合→通常のRSAと同様、鍵を作っている。
- これ解けたかもしれない…挑戦しておけばよかった…
- 高々10^4オーダーの計算でp,qが求まるので、そこから復号できる
- まず、pemから読み出しを行う
```
vagrant@vagrant:~/working/rsa/revolutional-secure-angou$ openssl rsa -pubin -in publickey.pem -text -noout
Public-Key: (2048 bit)
Modulus:
    00:85:29:06:3e:a0:ad:3b:46:29:6f:92:f7:23:56:
    77:2e:a4:e7:03:f7:b7:92:20:c1:8d:e1:b7:e3:ca:
    0a:77:28:d1:9e:69:dc:48:b8:68:5c:d6:04:f5:88:
    7a:4f:8f:3a:94:5a:1c:a1:59:3c:f0:86:d3:48:ec:
    4d:c9:21:42:08:3f:c9:e2:20:3c:65:30:31:1e:e5:
    10:be:50:a4:2a:ee:4a:63:e7:fa:66:bf:ce:35:12:
    fc:2f:b1:17:40:2a:55:cd:f0:89:77:70:c1:bb:86:
    f2:d9:30:6d:a5:b8:99:d2:94:ed:bc:b1:7a:d8:7e:
    17:59:2c:cc:3f:62:b1:30:57:24:18:17:32:ac:74:
    74:cf:23:be:b7:22:83:33:73:ef:07:b6:a9:21:88:
    cf:28:bc:fe:f2:6b:23:68:ad:a3:8f:7f:4f:d8:92:
    1d:be:3b:64:88:e4:b9:20:28:ff:bd:46:ae:26:d8:
    b4:3c:9a:86:db:bc:63:f0:b5:13:98:bb:54:09:8f:
    f7:00:4b:64:6a:fb:42:f2:43:54:ab:6a:2d:30:ef:
    ee:e8:b3:33:47:3a:be:1c:c9:2e:b6:8a:46:58:19:
    d9:e9:a0:ff:58:fe:af:2c:72:2a:e6:5b:7c:ed:c9:
    e3:0b:e9:15:02:9d:69:34:25:23:b9:81:ad:83:95:
    cd:f7
Exponent: 65537 (0x10001)
```
- Modulusがn
- めんどいのでCryptoパッケージ使いたい！
- 使った→solve.py参照。
- やってることは`_img/a.JPG, b.JPG`参照。
- 割と処理が遅いので、小さい数で実験しておくことと、昇順か降順かあたりをつけるのも大事だと感じた。
- [平方数判定高速化](http://d.hatena.ne.jp/yatt/20130128/1359370204)参考にした。
- try_square_root(e)でeが巨大でもsqrt(e)を返してくれるので使い勝手が良い。
- `TWCTF{9c10a83c122a9adfe6586f498655016d3267f195}` -> AC
