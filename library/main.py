from scripts.rot import ROT
f = open('cipher.txt', 'r')
string = f.read()
for i in range(26):
	print(ROT.rot(i, string))
