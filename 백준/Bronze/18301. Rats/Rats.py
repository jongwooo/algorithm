import sys

n1, n2, n12 = map(int, sys.stdin.readline().split())
print((n1 + 1) * (n2 + 1) // (n12 + 1) - 1)
