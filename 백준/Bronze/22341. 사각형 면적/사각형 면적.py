import sys

n, c = map(int, sys.stdin.readline().split())
a, b = n, n
for _ in range(c):
    x, y = map(int, sys.stdin.readline().split())
    if a <= x or b <= y:
        continue
    if a * y <= x * b:
        a = x
    else:
        b = y
print(a * b)
