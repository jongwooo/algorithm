import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
min_value = a[0]
for i in range(1, n):
    min_value = min(min_value, a[i])
    dp[i] = max(dp[i - 1], a[i] - min_value)
print(*dp)
