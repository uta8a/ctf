# fermat
import sys
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n//x) // 2
    return x

def is_square(n):
    if not n % 48 in (0,1,4,9,16,25,33,36):
        return False
    x = isqrt(n)
    return x*x == n

def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    while not is_square(b2):
        a += 1
        b2 = a*a - n
    return a - isqrt(b2)

if __name__ == '__main__':
    n = int(sys.argv[1])
    p = fermat(n)
    if p:
        print("{} = {} * {}".format(n, p, n/p))
    else:
        print("{} is prime".format(n))

