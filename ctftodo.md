# CTF TODO LIST
- CTFtime見ようね
- きちんと後から見て分かるように問題含めて完結するように書く。メモでもいいけど、最後にまとめを書く。

'''
過去問は以下にまとまっている。

    https://github.com/ctfs
    http://captf.com/

writeupを書く文化があるので、検索すれば解説が出てくるので安心。 知らなければ解けないような問題は多いので、一通り調べてみて方針が立たないようなら解説を見るべき、ということである。

また、pwn良問集(bata氏による)があるので、これを埋めていくとよさそう。
'''
- pwn埋め https://ctf.katsudon.org/ctf4u/

# 目標
- 広島CTF(抽選だけど)に行ったとき内容がわかるレベルになっておく(RE, radare2の使い方をわかるなど)
- 少なくともTJCTFとpicoCTFのできたやつ復習、まとめをしておきたいのでそれ最優先にする。
- pwnをやる(20日のめぐめぐ会までにある程度Harekazeを読む)
- デバッガの環境整備を急ぐ。CRCTFまでにRev, Pwnができるように、最低限のことはする。(Pwn初級やる、TWCTFEasyをする)
- 環境設定する(特にpython系をシステムのままやっているので、仮想環境の作りなおしをしたい。docker?で楽に作れるようにしておきたい)

# stack
- TJCTFの復習(理解の曖昧なpwnを理解する)→これは置いといて、easypwnから埋めていく
- picoCTF2017の復習
- めぐめぐ会の復習を記事にする。(ヒープ問)
- hackover, sectの復習

# config
- 基本はthinkpadX240か、windows上のVirtualBoxで進める(Project/ubuntu_16_04/ubuntu_16_04)
- vagrant up/vagrant halt
- githubと、開催中のCTFはgitlabで管理(git pullを忘れずに)