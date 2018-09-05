use_char = "0123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# base59 encode decode
import binascii
def base59enc(t): # t:text
	n = int(binascii.b2a_hex(t.encode('ascii')), 16) # text to base10
	b = ""
	while n > 0:
		b += use_char[n%59]
		n //= 59 # 割り算に注意
	return b[::-1]

def base59dec(t):
	n = 0
	for i in range(len(t)):
		n = 59 * n + use_char.index(t[i]) # n:10-based
	return binascii.a2b_hex(hex(n)[2:]) # hexにしてからasciiに変換

# import sys
# print(base59dec(base59enc(sys.argv[1]))) # テスト

ciphertext = "s7dwvcRrt10Jeo229BqE32ceU5pGaj9RRYCowVeTiKLfLZUjuQ7EQdAfiST9LQN2"

P = [
("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "Tjkv5wGzTRiJWWj5GaQ4e7A959icX1sFtWfwsTzmgLKYEGPFycQdLGgfUpd9EVGVD2qT"),
("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" , "TeEtfZWzTBqLDTMMsrqF9GaQq5tRQP7fi2LVHcNTdMEv1UhQ1oBhTQiuzEE2g4xbHXZ1"),
("cccccccccccccccccccccccccccccccccccccccccccccccccc", "T1WRL9MzTqEBfVcVWHji87zYxSQFyihxvSjomf2qzZ3QnFvoHpyUerLUJysppEcKEmb3"),
("dddddddddddddddddddddddddddddddddddddddddddddddddd", "T3vNg0nzDrY8z5sHq3YoaGJa2cHPbgg03b7hWXaHxfz5bt1TKkEYYpbR9V3YJpgYSCa8")
]
# 対応表を作る
M = {}
for p in P:
	b = base59enc(p[0])
	print(b)
	print(p[1])
	for i in range(len(b)):
		M[p[1][i]] = b[i]
print(M)

# flagの変換、decode
flag = "".join(M[c] for c in ciphertext)
print(ciphertext)
print(flag)
print(base59dec(flag)) # TWCTF{...}
