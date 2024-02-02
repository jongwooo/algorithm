import sys


def input():
    return sys.stdin.readline()


t = int(input())
for _ in range(t):
    n = int(input())
    c_sum, s_sum = 0, 0.0
    for _ in range(n):
        c, s = input().split()
        c_sum += int(c)
        s_sum += float(s) * int(c)
    print(f'{c_sum} {s_sum / c_sum:.1f}')
