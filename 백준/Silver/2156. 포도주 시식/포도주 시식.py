import sys

n = int(sys.stdin.readline())
wine = [0] + [int(sys.stdin.readline()) for _ in range(n)]
if n == 1:
    print(wine[1])
elif n == 2:
    print(sum(wine))
else:
    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + wine[i - 1]) + wine[i]
        dp[i] = max(dp[i - 1], dp[i])
    print(dp[n])
