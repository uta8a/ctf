# with open('f.txt', 'rb') as f:
#     data = f.read()

# for key in range(256):
#     flag = ''
#     for i in range(len(data)):
#         flag += chr(ord(data[i]) ^ key)
#     print key, flag

from time import sleep
tx = [ 0x3f, 0x29, 0x2f, 0x38, 0x17, 0x5d, 0x0a, 0x33, 0x39, 0x33, 0x59, 0x5b, 0x58, 0x15, 0x33, 0x1e, 0x5d, 0x0b, 0x04, 0x5b, 0x33, 0x1b, 0x04, 0x5f, 0x1e, 0x5f, 0x33, 0x39, 0x33, 0x3e, 0x40, 0x33, 0x5b, 0x04, 0x5f, 0x02, 0x33, 0x1c, 0x5f, 0x5c, 0x1c, 0x00, 0x5f, 0x33, 0x1b, 0x5d, 0x00, 0x00, 0x33, 0x5f, 0x1a, 0x5f, 0x02, 0x5b, 0x19, 0x58, 0x00, 0x00, 0x15, 0x33, 0x0f, 0x5c, 0x01, 0x5f, 0x33, 0x5b, 0x5c, 0x33, 0x39, 0x11, 0x66]
for key in range(256):
    flag = ''
    for i in range(len(tx)):
        flag += chr(int(tx[i]) ^ key)
    print key, flag
    sleep(0.1) # 一気にやると表示されないものが発生するのでsleep挟む
