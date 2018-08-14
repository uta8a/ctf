# まとめ

- たぶん、`tjctf{}`の形をしているものを探すんだと思う。
- tjctf2018/Volatile_Virus/file_patched.dmpは重過ぎるのでgitで管理しない
- 復習は一日5個埋める(全部で44個ある)、最後の方はあきらめるのも肝心っぽい…
- huuugeまでやった。(難易度順)

# WriteUps
- https://kmh.zone/writeups/tjctf-2018/
- https://tcode2k16.github.io/blog/posts/tjctf-2018-writeup/
- https://www.reddit.com/r/securityCTF/comments/96u46h/tjctf_2018_writeups/
- https://www.youtube.com/playlist?list=PL1H1sBF1VAKVmrjF1uWh5wK9a2IzmUjPc
- https://medium.com/@mihailferaru2000/tjctf-2018-full-binary-exploitation-walk-through-a72a9870564e pwn
- https://gitlab.com/blevy/redpwn-ctf-writeups/blob/master/tjctf2018/Abyss.md abyss分かりやすい
- https://github.com/TheRealOddCoder/tjctf2018 learnmyflag
- https://gist.github.com/Alaska47/524812936e000868e409ffdfd7703068 volatilevirus
- http://blog.seekintoo.com/the-abyss-writeup.html the abyss
- https://github.com/Lev9L-Team/ctf/tree/master/2018-08-07_tjctf sarah

# 対応表
| Problem | Knowledge |
|:-------:|:---------:|
| Blank | source(html) |
| Trippy | strings, grep |
| Weird Logo | library(stegsolve) |
| Discord! | (join community) |
| Cookie Monster | Cookie |
| Central Savings Account | source(js), md5 |
| Vinegar | Vigenere, Esper(or BruteforceAttack) |
| Interference | GIMP, threshold, QR |
| Math Whiz | StackOverFlow |
| Nothing but Everything | 10-based, hex, ASCII, 同じ内容であることに気づく | 
| Caesars Compilation | library(wordsearch), ROT |
| Huuuuuge | nmap, git(clone, --depth) |
|  ||

# 後で見る
- Weird Logo: stegsolveについて調べる、代替を考える、仕組みを知る
- md5など、逆関数の存在するもののライブラリ化
- python2が多く何年かしたらやばいので、簡単なものはRustで書き直すとかやってみてもいいかも(Rustの単純なコードに慣れる、テストなどの練習になる)
- Caesars Compilation: 斜め上とかを取得するスクリプトを、wordsearchに付加する

# 飛ばしたもの
- learn my flag飛ばす
- Speedy Security
