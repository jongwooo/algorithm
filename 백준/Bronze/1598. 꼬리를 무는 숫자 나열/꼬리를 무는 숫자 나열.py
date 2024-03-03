import sys

a, b = map(int, sys.stdin.readline().split())
a -= 1
b -= 1
print(abs(a // 4 - b // 4) + abs(a % 4 - b % 4))
