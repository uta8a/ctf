lis1 = 'uucbxsimbjyaqyvzbzfdatshktkbde'
lis2 = 'tjctf'
l1 = list(lis1)[0:5]
#print(l1)
l2 = list(lis2)
#for i,j in zip(l1, l2):
#    print(-ord(i) + ord(j))
l = [25,15,0,18,8,22,5,18,20]
ll = list(lis1)
#for i in l1:
#    print(i)


p=[]
for k,i in enumerate(ll):
    j = k%9
    ch = ord(i)+l[j]
    #:print(l[j])
    if ch > ord('z'):
        ch = ch - 26
    p.append(chr(ch))
print(''.join(p))
a1 = list(lis1)[-7:-3]
#print(a1)
s1 = 'dple'
a2 = list(s1)
#for i,j in zip(a1,s1):
#    print(ord(j) - ord(i))
