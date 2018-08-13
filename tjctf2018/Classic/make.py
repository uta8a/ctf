import sys

p = 11326943005628119672694629821649856331564947811949928186125208046290130000912216246378177299696220728414241927034282796937320547048361486068608744598351187
q = 11326943005628119672694629821649856331564947811949928186125208046290130000912120768861173564277210907403841603312764378561200102283658817695884193223692869
e = 65537
n = p*q

def exgcd(x,y):
    r0,r1 = x,y
    a0,a1 = 1,0
    b0,b1 = 0,1
    while r1>0:
        q1 = r0/r1
        r2 = r0%r1
        a2 = a0-q1*a1
        b2 = b0-q1*b1
        r0,r1 = r1,r2
        a0,a1 = a1,a2
        b0,b1 = b1,b2
    return a0,b0,r0

d = exgcd(e,(p-1)*(q-1))[0] + (p-1)*(q-1)
exp1 = d % (p-1)
exp2 = d % (q-1)
coef = pow(q,p-2,p)

def int2bin(d):
    t = "%x"%d
    return (t if len(t)%2==0 else "0"+t).decode("hex")

def enclen(l):
    if l<0x80:
        return chr(l)
    else:
        t = int2bin(l)
        return chr(0x80+len(t))+t

def encint(n):
    t = int2bin(n)
    return "\x02"+enclen(len(t))+t

t = "".join(map(encint,[0,n,e,d,p,q,exp1,exp2,coef]))
t = "\x30"+enclen(len(t))+t

print("-----BEGIN RSA PRIVATE KEY-----")
print(t.encode("base64")[:-1])
print("-----END RSA PRIVATE KEY-----")