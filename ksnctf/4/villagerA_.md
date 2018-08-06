# Villager A
- http://taishi8117.github.io/2015/10/20/ksnctf-villager-A/
# 用語？
- fmt_vuln: format vulnerability(Format String Attackできるという意味)
# Assemblyを見る
- なぜprintfの後にputchar \n(0xa) が呼ばれているのか？
- printf("Hi, %s\n", input)すればいいのに…→ここで怪しさを感じる。FSBを発見
- アドレスはmain+72みたいに表示する
- ASLR(Address space layout randomization): OSのためのメモリ保護機構。https://ja.wikipedia.org/wiki/%E3%82%A2%E3%83%89%E3%83%AC%E3%82%B9%E7%A9%BA%E9%96%93%E9%85%8D%E7%BD%AE%E3%81%AE%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E5%8C%96 うーん何言ってるかわからねえ
- とにかく今回は、jneのフラグを折ることでfopenを発生させるのは厳しいらしい。[esp+0123]のようなスタックのアドレスを推測するのは困難らしい。
- スタック上から6thplaceだというのはAAAA %x,%x,%x,%x,%x,%x,%x,%x,%x,%xをして41414141が出てくる場所で分かる。
- 次はpythonのコードを理解する。

- GOT overwriteについて
- ももテクをubuntuでやる。
- http://inaz2.hatenablog.com/entry/2014/04/20/041453
- fsb.c作った 設定戻す方法わからなくて怖いので明日詳しく調査してからやろうと思う。
- `sudo sysctl -w kernel.randomize_va_space=0`はシステム全体に対して効果があるので、ASLR無効にした後は`sudo sysctl -w kernel.randomize_va_space=2`に戻す。
