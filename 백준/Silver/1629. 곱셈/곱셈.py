import sys


def power(b):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    k = power(b // 2) % c
    if b % 2 == 0:
        return k * k % c
    else:
        return k * k % c * a % c


a, b, c = map(int, sys.stdin.readline().split())
print(power(b))
