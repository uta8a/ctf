from requests.auth import HTTPBasicAuth
import requests

print requests.options('https://request_me.tjctf.org/').text

print requests.put('https://request_me.tjctf.org/', data = {'username':'abcde', 'password':'abcde'}).text

print requests.post('https://request_me.tjctf.org/', auth=HTTPBasicAuth('abcde', 'abcde')).text

print requests.delete('https://request_me.tjctf.org/', auth=HTTPBasicAuth('abcde', 'abcde')).text

