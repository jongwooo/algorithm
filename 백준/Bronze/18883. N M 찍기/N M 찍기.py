import sys

n, m = map(int, sys.stdin.readline().split())
num = 1
for _ in range(n):
    for _ in range(m):
        if num % m == 0:
            print(num, end='')
        else:
            print(num, end=' ')
        num += 1
    print()
