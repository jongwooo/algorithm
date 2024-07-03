import sys


def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


n = int(sys.stdin.readline())
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(gcd(a, b))
