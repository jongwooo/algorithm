import sys

n = int(sys.stdin.readline())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
prefix = [[0] * (i + 1) for i in range(n)]
for i in range(n):
    for j in range(len(triangle[i])):
        if i == 0:
            prefix[i][j] = triangle[i][j]
        elif j == 0:
            prefix[i][j] = triangle[i][j] + prefix[i - 1][j]
        elif j == len(triangle[i]) - 1:
            prefix[i][j] = triangle[i][j] + prefix[i - 1][j - 1]
        else:
            prefix[i][j] = max(prefix[i - 1][j - 1], prefix[i - 1][j]) + triangle[i][j]
print(max(prefix[n - 1]))
