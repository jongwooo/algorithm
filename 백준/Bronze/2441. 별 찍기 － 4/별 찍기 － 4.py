import sys

n = int(sys.stdin.readline())
for i in range(n + 1):
    print(' ' * i + '*' * (n - i))
