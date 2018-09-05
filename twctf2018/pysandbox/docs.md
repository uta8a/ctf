# pysandbox
```
let's break sandbox.
start from nc pwn1.chal.ctf.westerns.tokyo 30001
```

# do
- これはpyjail!!!解きたい!!!!
- [qiitaの記事](https://qiita.com/t2y/items/0964d01bf3db0233e3c1)を見ると、literal_evalの方が安全らしい→evalを使っているので、その脆弱性をつく？
- `python eval vulnarable`あたりで検索して[記事](http://vipulchaskar.blogspot.com/2012/10/exploiting-eval-function-in-python.html)を見つける
- `dir`あたりが実行できればよいのだけれど、そもそも`nc`でつながらない…詰み。
- つながった。
```
vagrant@vagrant:~$ nc pwn1.chal.ctf.westerns.tokyo 30001
a
vagrant@vagrant:~$ nc pwn1.chal.ctf.westerns.tokyo 30001
f
vagrant@vagrant:~$ nc pwn1.chal.ctf.westerns.tokyo 30001
1+1
2vagrant@vagrant:~$ nc pwn1.chal.ctf.westerns.tokyo 30001
1+1+^H^H
vagrant@vagrant:~$ nc pwn1.chal.ctf.westerns.tokyo 30001
dir(module)
Invalid inputvagrant@vagrant:~$
```
- こんな感じで実行される
- とりあえず`ls -al`したい
- `os.system("ls -al")`はinvalid inputではじかれるのでこれっぽい
- The Abyssを試したけどはじかれた
- `'__class__'`は通るので、文字列は許容される