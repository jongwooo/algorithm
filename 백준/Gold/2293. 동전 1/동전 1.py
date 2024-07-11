import sys

n, k = map(int, sys.stdin.readline().split())
coins = sorted([int(sys.stdin.readline()) for _ in range(n)])
dp = [0] * (k + 1)
dp[0] = 1
for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]
print(dp[k])
