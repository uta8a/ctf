def pow_k(x, n, MOD):
    """
    O(log n)
    """
    if n == 0:
        return 1

    K = 1
    while n > 1:
        if n % 2 != 0:
            K *= x
            K %= MOD
        x *= x
        x %= MOD
        n //= 2

    return K * x % MOD

c = 150815
d = 1941
N = 435979
print(pow_k(c, d, N))
