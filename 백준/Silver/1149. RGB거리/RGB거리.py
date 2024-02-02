import sys

n = int(sys.stdin.readline())
prices = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
r, g, b = [prices[0][0]], [prices[0][1]], [prices[0][2]]
for i in range(1, n):
    r.append(min(g[i - 1], b[i - 1]) + prices[i][0])
    g.append(min(r[i - 1], b[i - 1]) + prices[i][1])
    b.append(min(r[i - 1], g[i - 1]) + prices[i][2])
print(min(min(r[-1], g[-1]), b[-1]))
