import sys

n = int(sys.stdin.readline())
a, b = 1, 1
for _ in range(3, n + 1):
    a, b = b, a + b
print(b, n - 2)
