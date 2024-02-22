import sys

n = int(sys.stdin.readline())
p = [0] + list(map(int, sys.stdin.readline().split()))
dp = [p[i] for i in range(n + 1)]
for i in range(n + 1):
    for j in range(i + 1):
        dp[i] = min(dp[i], dp[j] + p[i - j])
print(dp[n])
