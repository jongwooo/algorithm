import sys


def count_2(x):
    cnt = 0
    while x > 0:
        x //= 2
        cnt += x
    return cnt


def count_5(x):
    cnt = 0
    while x > 0:
        x //= 5
        cnt += x
    return cnt


n, m = map(int, sys.stdin.readline().split())
two = count_2(n) - count_2(m) - count_2(n - m)
five = count_5(n) - count_5(m) - count_5(n - m)
print(min(two, five))
