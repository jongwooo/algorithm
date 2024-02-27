import sys

n = int(sys.stdin.readline())
point = [0] + [int(sys.stdin.readline()) for _ in range(n)]
if n <= 2:
    print(sum(point))
else:
    dp = [0] * (n + 1)
    dp[1] = point[1]
    dp[2] = point[1] + point[2]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + point[i - 1]) + point[i]
    print(dp[n])
