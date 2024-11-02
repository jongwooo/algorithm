import sys

n = int(sys.stdin.readline())
a, b, c, d = map(int, sys.stdin.readline().split())
print(((c - a) + (d - b)) * 2)
for _ in range(n - 1):
    ai, bi, ci, di = map(int, sys.stdin.readline().split())
    a, b = min(a, ai), min(b, bi)
    c, d = max(c, ci), max(d, di)
    print(((c - a) + (d - b)) * 2)
