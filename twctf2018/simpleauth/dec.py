import hashlib
import sys

def decryptMD5(testHash):
        s = []
        while True:
                m = hashlib.md5()
                for c in s:
                        m.update(chr(c).encode('utf-8'))
                hash = m.hexdigest()
                if hash == testHash:
                        return ''.join([chr(c) for c in s])
                wrapped = True
                print(''.join([chr(c) for c in s]))
                for i in range(0, len(s)):
                        s[i] = (s[i] + 1) % 75 +48
                        if s[i] != 48:
                                wrapped = False
                                break
                if wrapped:
                        s.append(0)

print(decryptMD5(sys.argv[1]))