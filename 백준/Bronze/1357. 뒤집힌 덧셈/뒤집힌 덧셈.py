import sys


def rev(num):
    return int(str(num)[::-1])


a, b = map(int, sys.stdin.readline().split())
print(rev(rev(a) + rev(b)))
