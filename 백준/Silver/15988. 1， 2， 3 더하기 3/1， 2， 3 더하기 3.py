import sys

t = int(sys.stdin.readline())
dp = [1, 2, 4]
for i in range(3, 1_000_001):
    dp.append((dp[i - 3] + dp[i - 2] + dp[i - 1]) % 1_000_000_009)
for _ in range(t):
    n = int(sys.stdin.readline())
    print(dp[n - 1])
