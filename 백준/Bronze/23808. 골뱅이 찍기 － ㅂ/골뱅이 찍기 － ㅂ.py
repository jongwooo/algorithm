import sys

n = int(sys.stdin.readline())
for _ in range(2 * n):
    print('@' * n + '   ' * n + '@' * n)
for _ in range(n):
    print('@' * (5 * n))
for _ in range(n):
    print('@' * n + '   ' * n + '@' * n)
for _ in range(n):
    print('@' * (5 * n))
