# i-love-heddha [web]
```
A continuation of the Ez-Web challenge. enjoy

207.154.226.40:8080
```

# do
- robots.txtを再び見て/flag/を見る
- http://207.154.226.40:8080/flag/flag.txt
- また`Cookie: isAllowed=false`なので、たぶんこの先にまたなにかある
```
vagrant@vagrant:~$ curl curl -i -H 'Cookie: isAllowed=true' http://207.154.226.40:8080/flag/flag.txt
curl: (6) Could not resolve host: curl
HTTP/1.1 200
Content-Type: text/plain;charset=UTF-8
Content-Length: 175
Date: Sat, 06 Oct 2018 22:46:06 GMT

<!DOCTYPE html>
        <head>
                <title>Wrong Browser detected</title>
        </head>
        <body>
                <p>You are using the wrong browser, 'Builder browser 1.0.1' is required</p>
        </body>
</html>
```

- `curl -i -H 'Cookie: isAllowed=true' -H 'User-Agent: Builder browser 1.0.1' http://207.154.226.40:8080/flag/flag.txt`

```
vagrant@vagrant:~$ curl -i -H 'Cookie: isAllowed=true' -H 'User-Agent: Builder browser 1.0.1' http://207.154.226./flag/flag.txt
HTTP/1.1 200
Content-Type: text/plain;charset=UTF-8
Content-Length: 183
Date: Sat, 06 Oct 2018 22:48:19 GMT

<!DOCTYPE html>
        <head>
                <title>Almost</title>
        </head>
        <body>
                <p>You are refered from the wrong location hackover.18 would be the correct place to come from.</p>
        </body>
</html>
```
- `curl -i -H 'Cookie: isAllowed=true' -H 'User-Agent: Builder browser 1.0.1' -H 'Referer:hackover.18' http://207.154.226.40:8080/flag/flag.txt`
```
vagrant@vagrant:~$ curl -i -H 'Cookie: isAllowed=true' -H 'User-Agent: Builder browser 1.0.1' -H 'Referer:hackover.18' http://207.154.226.40:8080/flag/flag.txt
HTTP/1.1 200
Content-Type: text/plain;charset=UTF-8
Content-Length: 44
Date: Sat, 06 Oct 2018 22:52:54 GMT

aGFja292ZXIxOHs0bmdyeVczYlMzcnYzclM0eXNOMH0=
```
- base64ぽい
- base64 decodeした
- `hackover18{4ngryW3bS3rv3rS4ysN0}` -> AC