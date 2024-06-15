import sys

a = sum(map(int, sys.stdin.readline().split()))
b = sum(map(int, sys.stdin.readline().split()))
print(max(a, b))
