import sys
from itertools import combinations

INF = int(1e9)


def dist(c):
    b = 0
    for h_idx in range(n):
        a = INF
        for c_idx in c:
            tmp = abs(x[h_idx] - x[c_idx]) + abs(y[h_idx] - y[c_idx])
            a = min(a, tmp)
        b = max(b, a)
    return b


n, k = map(int, sys.stdin.readline().split())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, sys.stdin.readline().split())
final = INF
for c in combinations(range(n), k):
    final = min(final, dist(c))
print(final)
