import sys

input = sys.stdin.readline

dp = [0, 1, 3]
for i in range(3, 1001):
    dp.append(dp[i - 1] + 2* dp[i - 2])
n = int(input())
print(dp[n] % 10007)
