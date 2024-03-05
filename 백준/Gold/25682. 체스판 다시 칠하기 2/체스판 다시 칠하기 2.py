import sys


def min_board(color):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                value = board[i][j] != color
            else:
                value = board[i][j] == color
            prefix[i + 1][j + 1] = prefix[i][j + 1] + prefix[i + 1][j] - prefix[i][j] + value
    min_cnt = 2_000 * 2_000
    for i in range(1, n - k + 2):
        for j in range(1, m - k + 2):
            cnt = prefix[i + k - 1][j + k - 1] - prefix[i + k - 1][j - 1] - prefix[i - 1][j + k - 1] + prefix[i - 1][
                j - 1]
            min_cnt = min(min_cnt, cnt)
    return min_cnt


n, m, k = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
print(min(min_board('B'), min_board('W')))
