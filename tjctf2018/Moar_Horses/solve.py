import requests

url = "https://moar_horse.tjctf.org/legs"
a = 0
while True:
    a+=1
    print(a)
    res = requests.get(url).text
    if "Oops" not in res:
        print(res)
        break
