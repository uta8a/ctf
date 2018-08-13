key = open("firstpartoftheflag.txt", 'r').readline().strip()
ivmes = open("somenicesentences.txt", 'r').read().split('\n')[:-1]
iv = [""]*6
for x in range(len(key)):
	for y in range(len(ivmes)):
		iv[y] += str(ord(ivmes[y][x])^ord(key[x]))
rsaexp = open("e.txt", 'r').read().split()
rsamod = open("n.txt", 'r').read().split()
rsact = open("c.txt", 'r').read().split()

out = open("terms.txt", 'w')
for z in range(len(rsaexp)):
	newe = int(rsaexp[z])*int(ivmes[z].encode('hex'), 16)-256
	out.write("masked e = " + str(newe) + '\n')
	out.write("beta = " + iv[z] + '\n')
	out.write("n = " + rsamod[z] + '\n')
	out.write("c = " + rsact[z] + '\n')

