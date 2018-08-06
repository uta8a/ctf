# Python
- 今回使ったのはrequestsのみ。
- 適当にidとpass入れてリクエスト送るやつを一から作ってみる。
- あと注意として、`'`をエスケープしてやる必要がある。→`\'`

# 使ったもの(pseudo code)
```
import requests
url = 'http...'
payload={
    'id': id,      # ここが'id'であることはphpのソースコードから分かったこと。
    'pass': pass   # ここも、'password'とかじゃなく'pass'なのはphpのソースコードから分かったこと。
}
response = requests.post(url, data=payload)
print(response.text)
```
- だいたいこんな感じで、payloadを工夫してリクエストを送る。