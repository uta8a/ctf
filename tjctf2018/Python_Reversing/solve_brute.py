import string
import numpy as np


# flag = 'redacted'

original_output = '1001100001011110110100001100001010000011110101001100100011101111110100011111010101010000000110000011101101110000101111101010111011100101000011011010110010100001100010001010101001100001110110100110011101'
# original_output = '10011000010111101101000011000010100000111' # this is encrypted tjctf


def encrypt(string):
	np.random.seed(12345)
	arr = np.array([ord(c) for c in string])
	other = np.random.randint(1,5,(len(string)))
	arr = np.multiply(arr,other)

	b = [x for x in arr]
	lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
	c = [b[i]^lmao[i] for i,j in enumerate(b)]
	return(''.join(bin(x)[2:].zfill(8) for x in c))

print encrypt('tjctf')

flag = list('tjctf{')

while(1):
	for character in string.printable:
		print ''.join(flag) + character
		out = encrypt(''.join(flag) + character )
		if original_output.startswith(out):
			flag.append(character)
			print 'GOT,'
			print ''.join(flag)
			break
