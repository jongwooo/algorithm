import sys

n = int(sys.stdin.readline())
dp = [i for i in range(n + 1)]
for i in range(n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], dp[i - j * j] + 1)
print(dp[n])
