import sys

a = int(sys.stdin.readline())
b = sorted(list(map(int, sys.stdin.readline().split())))
print(b[(a - 1) // 2] ** 2 if a % 2 == 1 else b[0] * b[-1])
