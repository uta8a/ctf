# CRCTFの感想
- CyberRebeatCTFにチームGrowthKeysで参加しました。チームで参加したのは初めてだったので楽しかったです。
- 個人で出てるときはまったりとやってあー解けなかった、Writeup待とうみたいな感じで途中で投げちゃうのですがチームだと自分が担当？と思ってる問題もガンガン手をつけられていくので焦りがあり、とてもよい緊張感の中追い立てられるように集中できてよかったです。最後まで粘れたのはよかった。
- とはいえ、実質2問しか解けなかった…難しい問題を眺めている時間が長すぎたので解ききるためにもっと強くなりたいです。flagが取れないと無なので。
- このくらいの難易度が初心者的にうれしいです。作者の方がバイナリ以外作問されたとのことで、すごい…。
- writeup…というほどのものでもないですが、書きます。バイナリはかなり丁寧に書いてみました。

### SimpleBinary
```
SimpleBinary
```
- バイナリファイルが渡されます。
- radare2を使っていきます
- まずはデバッグモード(-d)でバイナリを開きましょう
```
r2 -d SimpleBinary
```
- 初手aaaaです(分析をするフェーズで、とりあえず開いたらやります)
```
aaaa
```
- mainに飛んで、main関数のディスアセンブルをします
```
s main
pdf
```
- 眺めていると、以下のように怪しい文字列を発見します
```
0x004006d1      48b87b694343.  movabs rax, 0x69732e204343697b ; '{iCC .si'
0x004006df      48b874682074.  movabs rax, 0x4620752774206874 ; 'th t'u F'
0x004006ed      48b86e7d6449.  movabs rax, 0x6167546d49647d6e ; 'n}dImTga'
0x004006fb      66c745e85268   mov word [local_18h], 0x6852 ; 'Rh'
```
- このままでは意味が通らないのですが、`{}`のようにいかにもflagっぽいので、"処理をした後のスタックを見る"という典型を思い出してbreakpointを仕掛けます
- breakpointとは、最後まで実行するのではなく、途中まで処理を進めてストップさせるというものです
- breakpointをどこに仕掛けるかですが、処理がどこまで続いているかわからないので、`0x00400732      7405           je 0x400739`とジャンプして終了してしまう直前の`0x00400729`を選びました。
- `db [address]`でbreakpointを仕掛けて、`dc`でbreakpointまで実行させます
```
db 0x00400729
dc
```
- スタックポインタは`rsp`なので、メモリの中身を表示してくれる`pxr @ [address]`を使ってスタックの中身を見ます
```
pxr @ rsp
```
- 中身を見ると@rdi asciiのところから`CRCTF{...`と見えます。flag `CRCTF{It's a humid night.}`->AC
```
0x7ffefdafce00  0x00007ffefdafcf38   8....... @rsp stack R W 0x7ffefdafe6c8 -->  stack R W 0x656c706d69532f2e (./SimpleBinary) -->  ascii
0x7ffefdafce08  0x000000016f736476   vdso....
0x7ffefdafce10  0x0000000000000001   ........
0x7ffefdafce18  0x0000001b0040078d   ..@.....
0x7ffefdafce20  0x74497b4654435243   CRCTF{It @rdi ascii
0x7ffefdafce28  0x6d75682061207327   's a hum ascii
0x7ffefdafce30  0x746867696e206469   id night ascii
0x7ffefdafce38  0x0000000000007d2e   .}...... ascii
0x7ffefdafce40  0x00007ffefdafcf30   0....... r13 stack R W 0x1
0x7ffefdafce48  0x2010cbacc6f98d00   .......  rcx
0x7ffefdafce50  0x0000000000400740   @.@..... @rbp (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) program R X 'push r15' 'SimpleBinary'
0x7ffefdafce58  0x00007f1cd1a00830   0.......
0x7ffefdafce60  0x0000000000000000   ........ esp
0x7ffefdafce68  0x00007ffefdafcf38   8....... stack R W 0x7ffefdafe6c8 -->  stack R W 0x656c706d69532f2e (./SimpleBinary) -->  ascii
0x7ffefdafce70  0x0000000100000000   ........
0x7ffefdafce78  0x00000000004006b3   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) main main program R X 'push rbp' 'SimpleBinary'
0x7ffefdafce80  0x0000000000000000   ........ esp
0x7ffefdafce88  0x7526e24ea3da1f02   ....N.&u
0x7ffefdafce90  0x0000000000400450   P.@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) r12 entry0 program R X 'xor ebp, ebp' 'SimpleBinary'
0x7ffefdafce98  0x00007ffefdafcf30   0....... r13 stack R W 0x1
0x7ffefdafcea0  0x0000000000000000   ........ esp
0x7ffefdafcea8  0x0000000000000000   ........ esp
0x7ffefdafceb0  0x8adb1991319a1f02   ...1....
0x7ffefdafceb8  0x8b1f418ea28a1f02   .....A..
0x7ffefdafcec0  0x0000000000000000   ........ esp
0x7ffefdafcec8  0x0000000000000000   ........ esp
0x7ffefdafced0  0x0000000000000000   ........ esp
0x7ffefdafced8  0x0000000000000001   ........
0x7ffefdafcee0  0x00000000004006b3   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) main main program R X 'push rbp' 'SimpleBinary'
0x7ffefdafcee8  0x00000000004007b0   ..@..... (LOAD0) (/home/vagrant/crctf/crctf/SimpleBinary) r8 program R X 'ret' 'SimpleBinary'
0x7ffefdafcef0  0x0000000000000000   ........ esp
0x7ffefdafcef8  0x0000000000000000   ........ esp
```

### FLAG.encrypted
```
Get the FLAG.


FLAG.encrypted
public-key.pem
```
- RSA問です。pycryptoパッケージを使ってpemからeとnを取り出すとeが大きい(たいていeは65537)ことが分かり、wiener's attackが使えると分かります。
- owienerを使いました(適当にググるといろいろ出てくるので落としてきましょう)
```
import owiener

e = 22766071057080311941289025090582171055356241374729867687887721165996480747230400879635593368509050250879664911119593845131632736205037337764476149970317207453325852306744743355843865620488975017552101697514723815810433086583097066849281143179649731453788074604410013059110037363738062212112776408805474047616975914133565204728262194785129197335550911873746857764241100489778203898866941412395489839653170240092405989209278646213522785197290066584628647242197250525516210135602818305240062919066210956719110372916047407851800476348031106117342132809755720425300509425412742257946576118121595189882915440991231610926049
n = 31264943211208004265136257812922871300684039354012330190834942986731934389912197706421706868451670101634969269274623828581050676733228020854883441494567900924428451571798331504026565707472121772002140681756280190535290943933921834846379665606960802397274296703426557981596105415677658499356618548233939389723076124471098440146923189296244078349641695576997335766674231277153794543785116533620076935082137870329278026757983028280620935089387958708697459641119539250284149601503334899598799831125405703179815161182156366487341348125463136351944709488739527831476641990338237417959538685045943046162779336438891834429341
d = owiener.attack(e, n)

if d is None:
    print("Failed")
else:
    print("Hacked d={}".format(d))
```
- 復号です
```
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from Crypto.Cipher import PKCS1_v1_5
e = 22766071057080311941289025090582171055356241374729867687887721165996480747230400879635593368509050250879664911119593845131632736205037337764476149970317207453325852306744743355843865620488975017552101697514723815810433086583097066849281143179649731453788074604410013059110037363738062212112776408805474047616975914133565204728262194785129197335550911873746857764241100489778203898866941412395489839653170240092405989209278646213522785197290066584628647242197250525516210135602818305240062919066210956719110372916047407851800476348031106117342132809755720425300509425412742257946576118121595189882915440991231610926049
n = 31264943211208004265136257812922871300684039354012330190834942986731934389912197706421706868451670101634969269274623828581050676733228020854883441494567900924428451571798331504026565707472121772002140681756280190535290943933921834846379665606960802397274296703426557981596105415677658499356618548233939389723076124471098440146923189296244078349641695576997335766674231277153794543785116533620076935082137870329278026757983028280620935089387958708697459641119539250284149601503334899598799831125405703179815161182156366487341348125463136351944709488739527831476641990338237417959538685045943046162779336438891834429341
d = 455331605442542025389272451598784612768671576303996772922270683577044948094011818131938476204941161531733636881514994041550943735995251876760125998519977
privkey = RSA.construct((n, e, d))
print PKCS1_v1_5.new(privkey).decrypt(open("FLAG.encrypted", "rb").read(), "!")
```


