# note
- web問での話
`例えば、UUIDを入力に受け付けるWeb問があったとして
単純に英数字入力するのをやめて、途中にNULL文字を含めてみたり、UUIDの形式を守らずにやってみたり、違うバージョンのものを試してみたり、色んな入力を与えてみることですね。
(もしできたら、Pythonとかで自動スクリプトを組めるといい。)`
- curlも使える

# smth_revengeに関して
- これはディレクトリ構成によっては動かないこともあるので注意。また、ubuntu16.04で動いて18.04ではSEGVした。
```
straceを使うと分かりますが、確か /home/smth_revenge/flag が存在しないことによるエラーでしたので、 
前者の方法だと
sudo mkdir -p /home/smth_revenge && sudo echo "CTF{flag_is_here}" > /home/smth_revenge/flag
とやると解決できて
後者の方法では、 バイナリファイル中の文字列 "/home/smth_revenge/flag" を上書きして、"./flag\x00"とすると現在のディレクトリに flagファイルを作ることで済むので、 radare2 をwオプション付で開いて該当する文字列を書き換えることで開くファイルを変更することが出来ます。
```
- 今回は、前者の方法で解決した。
## やったこと
- /home/smth_revengeディレクトリの作成
- chown -R vagrant:vagrant smth_revenge で権限を変更
- smth_revengeディレクトリに移動し、echo "CTF{flag_is_here}" > flag
- wgetでバイナリを引っ張ってくる→名前変更が&とかのせいでできなかったけど、それでも動くのでそのまま
- uc?...という名前になった
- chmod +x uc?...
- ./uc?... 実行
- 動いた