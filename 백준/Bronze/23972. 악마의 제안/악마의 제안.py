import sys

k, n = map(int, sys.stdin.readline().split())
if n == 1:
    print(-1)
else:
    x = (n * k) // (n - 1)
    if (n * k) % (n - 1):
        x += 1
    print(x)
