import string

message = "[REDACTED][REDACTED][REDACTED]abcdefg"
key = "abcde"


def e(message, key):
  l = len(key)
  s = [message[i::l] for i in range(l)]
  print s
  for i in range(l):
    a = 0
    e = ''
    for c in s[i]:
      a = ord(c) ^ ord(key[i]) ^ (a >> 2)
      e += chr(a)
    s[i] = e

  # print s
  # print(zip(*s))
  # print "".join("".join(y) for y in zip(*s))
  return "".join(hex((1 << 8)+ord(f))[3:] for f in "".join("".join(y) for y in zip(*s)))

def crack(message):
  startText = 'tjctf{'
  possibleKeyLength = [1, 2, 4, 7, 8, 14, 28, 56]

  for l in possibleKeyLength:
    key = ''
    chars = [ chr(int(message[x:x+2], 16)) for x in range(0, len(message), 2) ]
    splitCipher = lambda A, n: [tuple(A[i:i+n]) for i in range(0, len(A), n)]
    chars = splitCipher(chars, l)
    chars = zip(*chars)
    for i in range(min(len(startText), len(chars))):
      key += chr(ord(chars[i][0]) ^ ord(startText[i]))
    print key
    
def d(message, key):
  l = len(key)
  chars = [ chr(int(message[x:x+2], 16)) for x in range(0, len(message), 2) ]
  splitCipher = lambda A, n: [tuple(A[i:i+n]) for i in range(0, len(A), n)]
  chars = splitCipher(chars, l)
  chars = zip(*chars)
  # print chars
  for i in range(l):
    a = 0
    e = ''
    for charI in range(len(chars[i])):
      if a == 0:
        a = ord(chars[i][charI]) ^ ord(key[i]) ^ (a >> 2)
      else:
        a = ord(chars[i][charI]) ^ ord(key[i]) ^ (ord(chars[i][charI-1]) >> 2)
      e += chr(a)
    chars[i] = e

  final = ''
  for a in range(len(chars[0])):
    for b in range(len(chars)):
      final += chars[b][a]
  return final

c = e(message, key)
print c
print d(c, key)
print crack('473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554')
print d('473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554', '3V@mK<aa')

# got keyLength = 8

for a in string.printable:
  for b in string.printable:
    flag = d('473c23192d4737025b3b2d34175f66421631250711461a7905342a3e365d08190215152f1f1e3d5c550c12521f55217e500a3714787b6554', '3V@mK<'+a+b)
    if flag[-1] == '}':
      print flag
