a = list(input())
b=[]
for i in a:
    if i==" " or i==".":
        b.append(i)
    else:
        p = ord(i)
        if p >= 97:
            if p - 97 >= 13:
                b.append(chr(p-13))
            else:
                b.append(chr(p+13))
        elif p >= 65:
            if p-65 >= 13:
                b.append(chr(p-13))
            else:
                b.append(chr(p+13))
print(''.join(b))
# chr(ord(i)-13)
"""
# writeup
スペースがあるしなにかの置換暗号をまず疑う。
Synt vfがなんか怪しいのでこれFlag isでしょとアタリをつける
素直にascii変換-13して、chr(ord(i) - 13)する
→うまくいかない
よく見ると、vfがisになってない→小文字は小文字内で、大文字は大文字内で循環しているっぽい
" "と,は無視して循環させる
ROT XIII is a simple letter substitution cipher that replaces a letter with the letter XIII letters after it in the alphabet. ROT XIII is an example of the Caesar cipher developed in ancient Rome. Flag is FLAGSwzgxBJSAMqwxxAU. Insert an underscore immediately after FLAG.
それっぽいの出てきた
ROT13というらしい。コピペする
→失敗
underscoreいれてねとのこと。FLAG_SwzgxBJSAMqwxxAUを入れる
→成功
"""
