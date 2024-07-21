import sys

a, b, c = map(int, sys.stdin.readline().split())
print(a * max(b, c) // min(b, c))
