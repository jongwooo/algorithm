import sys


def mul(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k] * b[k][j]
            result[i][j] = num % 1_000_000_000
    return result


def power(n):
    fib = [[1, 1], [1, 0]]
    if n == 1:
        return fib
    x = power(n // 2)
    if n % 2 == 0:
        return mul(x, x)
    return mul(mul(x, x), fib)


a, b = map(int, sys.stdin.readline().split())
print((power(b + 2)[1][0] - power(a + 1)[1][0]) % 1_000_000_000)
