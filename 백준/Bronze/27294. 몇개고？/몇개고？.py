import sys

t, s = map(int, sys.stdin.readline().split())
print(320 if 12 <= t <= 16 and s == 0 else 280)
