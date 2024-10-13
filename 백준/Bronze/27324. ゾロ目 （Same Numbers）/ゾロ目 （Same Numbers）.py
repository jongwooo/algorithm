import sys

n = int(sys.stdin.readline())
print(1 if n // 10 == n % 10 else 0)
