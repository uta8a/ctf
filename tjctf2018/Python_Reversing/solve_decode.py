from itertools import *
import numpy as np

def decode(message):
  lmao = [ord(x) for x in ''.join(['ligma_sugma_sugondese_'*5])]
  for l in combinations([x for x in range(19, 25)], 0):
    counter = 19
    index = 0
    arr = [304, 189, 161, 133, 7, 169, 291, 382, 143, 341, 1, 131, 366, 23, 427, 370, 134, 428, 161]
    isGood = True
    while counter < 25:
      if counter in l:
        if message[index:index+9][0] == '0':
          isGood = False
        arr.append(int(message[index:index+9], 2))
        index += 9
      else:
        arr.append(int(message[index:index+8], 2))
        index += 8
      counter += 1
    # if not isGood:
    #   break
    # print l
    print(arr)
    arr = [j^lmao[i] for i , j in enumerate(arr)]
    # print(arr)
    np.random.seed(12345)
    arr = np.array(arr)
    other = np.random.randint(1,5,(len(arr)))
    arr = np.divide(arr, other).tolist()
    print ''.join([chr(x) for x in arr])

  # splitCipher = lambda A, n: [A[i:i+n] for i in range(0, len(A), n)]
  # chars = splitCipher(message, 8)
  # print chars

decode('100010001010101001100001110110100110011101')
