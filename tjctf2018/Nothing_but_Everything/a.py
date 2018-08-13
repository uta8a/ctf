from glob import glob
import os

directory ='1262404985085867488371'

def clarify(number):
    return hex(int(number))[2:].replace('L','').decode('hex')

print clarify('1466921579')
print clarify('74145705061991')
# os.chdir(directory + '/74145705061991')
for i in os.listdir('.'):
    try:
        print clarify(i)
#        c = open(i).read()
#        open(clarify(i), 'w').write(clarify(c))
    except:
        print "FAILED WITH", i
