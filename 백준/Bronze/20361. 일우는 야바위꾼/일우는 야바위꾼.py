import sys

n, x, k = map(int, sys.stdin.readline().split())
cup = [i + 1 for i in range(n)]
change = [tuple(map(int, sys.stdin.readline().split())) for _ in range(k)]
for i in range(k):
    cup[change[i][0] - 1], cup[change[i][1] - 1] = cup[change[i][1] - 1], cup[change[i][0] - 1]
print(cup.index(x) + 1)
