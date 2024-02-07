import sys

a, b = map(int, sys.stdin.readline().split())
sq = []
for i in range(1, b + 1):
    for j in range(i):
        sq.append(i)
print(sum(sq[a - 1:b]))
