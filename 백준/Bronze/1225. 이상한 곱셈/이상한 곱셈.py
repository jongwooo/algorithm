import sys

A, B = sys.stdin.readline().split()
a = list(map(int, A))
b = list(map(int, B))
print(sum(a) * sum(b))
