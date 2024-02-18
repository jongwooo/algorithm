import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())
a = a1 * b2 + a2 * b1
b = b1 * b2
print(a // gcd(a, b), b // gcd(a, b))
