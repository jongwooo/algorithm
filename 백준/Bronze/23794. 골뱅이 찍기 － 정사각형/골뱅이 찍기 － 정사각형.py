import sys

n = int(sys.stdin.readline())
print('@' * (n + 2))
for _ in range(n):
    print('@' + ' ' * n + '@')
print('@' * (n + 2))
