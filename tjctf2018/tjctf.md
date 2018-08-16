# まとめ

- たぶん、`tjctf{}`の形をしているものを探すんだと思う。
- tjctf2018/Volatile_Virus/file_patched.dmpは重過ぎるのでgitで管理しない
- 復習は一日5個埋める(全部で44個ある)、最後の方はあきらめるのも肝心っぽい…

# WriteUps
- https://kmh.zone/writeups/tjctf-2018/ The Abyss
- https://tcode2k16.github.io/blog/posts/tjctf-2018-writeup/
- https://www.reddit.com/r/securityCTF/comments/96u46h/tjctf_2018_writeups/
- https://www.youtube.com/playlist?list=PL1H1sBF1VAKVmrjF1uWh5wK9a2IzmUjPc これは完了。22問分載ってる
- https://medium.com/@mihailferaru2000/tjctf-2018-full-binary-exploitation-walk-through-a72a9870564e pwn
- https://gitlab.com/blevy/redpwn-ctf-writeups/blob/master/tjctf2018/Abyss.md abyss分かりやすい
- https://github.com/TheRealOddCoder/tjctf2018 learnmyflag
- https://gist.github.com/Alaska47/524812936e000868e409ffdfd7703068 volatilevirus
- http://blog.seekintoo.com/the-abyss-writeup.html the abyss
- https://github.com/Lev9L-Team/ctf/tree/master/2018-08-07_tjctf sarah
- http://blog.seekintoo.com/the-abyss-writeup.html the abyss
- https://github.com/Lev9L-Team/ctf/tree/master/2018-08-07_tjctf mirror sarah
- https://github.com/jazon-liu/ctf-writeups/tree/master/tjctf-2018 (many)
- https://shrekisloveshrekis.life/tjctf/ stupidblog


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
| Learn My Flag ||
| Request Me | HTTP(GET,POST,PUT,DELETE) |
| Validator | radare2, ltrace, strcmp |
| Classic | RSA(Fermat), hex |
| Speedy Security ||
| Python Reversing | encryptしてみる、比較する、Brute-Force-Attack |
| Ess Kyoo Ell | SQLinjection(column), Esper, username='admin' |
| Tilted Troop | game, ASCII |
| Lexington State Bank | LSB |
| RC4 took an L ||
| Moar Horses | 何回もRequest送る |
| Grid Parser ||
| Bad Cipher | Brute-Force-Attack, key長の特定 |
| Weird Audio Circuit ||
| Sarahs Cryptosystem ||
| Programmable Hyperlinked Pasta | directory(proc/self/cwd) |
| Permutations ||
| Ssleepy | pcapng, TCP, SSL, jpg(ffd8) |
| We Will Rock You |  |
| PIT or Miss ||
| Bricked Binary | 分からない(binary patch) |
| Future Canary Lab | rand(), exploit(pwnと別に書くタイプ) |
| Moar Turtles ||
| Affine | |
| Online Banking | buffer overflow, radare2(i~nx) |
| Mirror Mirror | python jail |
| Secure Secrets | FSB, GOT, radare2(afl)|
| Volatile Virus ||
| Stupid Blog ||
| Super Secure Secrets ||
| The Abyss | python jail |

# 後で見る
- Weird Logo: stegsolveについて調べる、代替を考える、仕組みを知る
- md5など、逆関数の存在するもののライブラリ化
- python2が多く何年かしたらやばいので、簡単なものはRustで書き直すとかやってみてもいいかも(Rustの単純なコードに慣れる、テストなどの練習になる)
- Caesars Compilation: 斜め上とかを取得するスクリプトを、wordsearchに付加する
