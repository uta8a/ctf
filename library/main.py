from scripts.rot import ROT
# f = open('a.txt', 'r')
# string = f.read()
string = "txpgs{V_nz_CNPXZNA}"
for i in range(26):
	print(ROT.rot(i, string))
