from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from Crypto.Cipher import PKCS1_v1_5

pubkey = RSA.importKey(open("publickey.pem").read()).publickey()
e = pubkey.e
n = pubkey.n

# print e
# print n

def bisearch(f, n):
    l = 0
    r = n
    fl = f(l)
    fr = f(r)
    while l <= r:
        m = (l + r) // 2
        fm = f(m)
        #print l,m,r,fl,fm,fr,n
        if fm == n:
            return m
        elif fm > n:
            r = m - 1
            fr = f(r)
        else:
            l = m + 1
            fl = f(l)

def try_square_root(n2):
    return bisearch(lambda n:n*n, n2)

import math
for k in range(e)[::-1]:
	if k==0:
		continue
	else:	
		break
		print k	
		if try_square_root(4*e*k*n  + 1):
			print k
			p = (math.sqrt(4*e*k*n+1) - 1)/(2*k)
			print p
			q = n/p
			print q
			d = inverse(e, (p-1)*(q-1))

			print d
			
			privkey = RSA.construct((n, e, d))
			print PKCS1_v1_5.new(privkey).decrypt(open("flag.encrypted", "rb").read(), "!")
			break
	
k = 54080
print try_square_root(4*e*k*n + 1)
p = (try_square_root(4*e*k*n+1) - 1) / (2*k)
q = n/p
d = inverse(e, (p-1)*(q-1))
print p
print q
print d
privkey = RSA.construct((n, e, d))
print PKCS1_v1_5.new(privkey).decrypt(open("flag.encrypted", "rb").read(), "!")	
