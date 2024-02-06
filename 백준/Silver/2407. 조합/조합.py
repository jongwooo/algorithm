import sys


def factorial(n):
    num = 1
    for i in range(1, n + 1):
        num *= i
    return num


def combination(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))


n, m = map(int, sys.stdin.readline().split())
print(combination(n, m))
