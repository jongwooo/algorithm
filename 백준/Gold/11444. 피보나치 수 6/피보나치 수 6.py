import sys


def fibonacci(n):
    if n in f:
        return f[n]
    if n % 2 == 0:
        val = fibonacci(n // 2) * (2 * fibonacci(n // 2 - 1) + fibonacci(n // 2))
    else:
        val = fibonacci((n + 1) // 2) ** 2 + fibonacci((n - 1) // 2) ** 2
    f[n] = val % 1_000_000_007
    return f[n]


n = int(sys.stdin.readline())
f = {0: 0, 1: 1}
print(fibonacci(n))
