import sys

w = sorted([int(sys.stdin.readline()) for _ in range(10)])
k = sorted([int(sys.stdin.readline()) for _ in range(10)])
print(sum(w[7:]))
print(sum(k[7:]))
