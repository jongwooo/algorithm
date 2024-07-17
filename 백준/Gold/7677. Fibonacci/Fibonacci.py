import sys


def mul(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k] * b[k][j]
            result[i][j] = num % 10_000
    return result


def power(b):
    fib = [[1, 1], [1, 0]]
    if b == 1:
        return fib
    x = power(b // 2)
    if b % 2 == 0:
        return mul(x, x)
    return mul(mul(x, x), fib)


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        print(0)
    elif n == -1:
        break
    else:
        print(power(n)[1][0])
