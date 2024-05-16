import sys

d, p = map(int, sys.stdin.readline().split())
dp = [int(1e9)] + [0] * d
for _ in range(p):
    l, c = map(int, sys.stdin.readline().split())
    copied = dp.copy()
    for i in range(l, d + 1):
        if copied[i - l]:
            dp[i] = max(dp[i], min(copied[i - l], c))
print(dp[d])
