import sys


def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


a, b = map(int, sys.stdin.readline().split())
print('1' * gcd(a, b))
