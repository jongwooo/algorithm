import sys

a, b, c, n = map(int, sys.stdin.readline().split())
dp = [0] * 301
dp[a] = dp[b] = dp[c] = 1
for i in range(a, n + 1):
    for j in (a, b, c):
        if i >= j and dp[i - j]:
            dp[i] = 1
print(dp[n])
