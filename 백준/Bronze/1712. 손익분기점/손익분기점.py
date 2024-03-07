import sys

a, b, c = map(int, sys.stdin.readline().split())
print(-1 if c <= b else a // (c - b) + 1)
