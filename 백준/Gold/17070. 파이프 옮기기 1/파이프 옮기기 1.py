import sys

n = int(sys.stdin.readline())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[[0] * n for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, n):
    if grid[0][i] == 0:
        dp[0][0][i] = dp[0][0][i - 1]
for r in range(1, n):
    for c in range(1, n):
        if grid[r][c] == 0 and grid[r][c - 1] == 0 and grid[r - 1][c] == 0:  # 대각선
            dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]
        if grid[r][c] == 0:  # 가로, 세로
            dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
            dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]
print(sum(dp[i][n - 1][n - 1] for i in range(3)))
