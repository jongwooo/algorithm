import sys

N = int(sys.stdin.readline())
t_and_p = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if i + t_and_p[i][0] > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], t_and_p[i][1] + dp[i + t_and_p[i][0]])
print(dp[0])
