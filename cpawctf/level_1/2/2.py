l = list(input())
b=[]
for i in l:
    if i=="{" or i== "}" or i=="_":
        b.append(i)
    j = ord(i)
    if j >= 97:
        if j-97 >= 0:
            b.append(chr(j - 3))
        else:
            b.append(chr(j - 3 + 26))
    else:
        if j-65 >= 0:
            b.append(chr(j - 3))
        else:
            b.append(chr(j - 3 + 26))
print(''.join(b))
