import sys

MAX_NUM = 1_000_000
dp = [0] * (MAX_NUM + 1)
g = [0] * (MAX_NUM + 1)
for i in range(1, MAX_NUM + 1):
    for j in range(1, (MAX_NUM // i) + 1):
        dp[i * j] += i
    g[i] = g[i - 1] + dp[i]
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(g[n])
