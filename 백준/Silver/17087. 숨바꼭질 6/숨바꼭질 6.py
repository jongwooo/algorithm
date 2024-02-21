import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
d = [abs(s - i) for i in a]
g = d[0]
for i in range(1, len(d)):
    g = gcd(g, d[i])
print(g)
