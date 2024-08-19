import sys

n = int(sys.stdin.readline())
for _ in range(1, n + 1):
    print('@@@@@' * n)
for _ in range(1, n * 3 + 1):
    print('@' * n)
for _ in range(1, n + 1):
    print('@@@@@' * n)
