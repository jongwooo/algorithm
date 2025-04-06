import sys


def check_cur_max_cnt():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        cnt = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
    return max_cnt


n = int(sys.stdin.readline())
board = [list(sys.stdin.readline()) for _ in range(n)]
total_max_cnt = 1
for i in range(n):
    for j in range(n - 1):
        if j + 1 < n and board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            total_max_cnt = max(total_max_cnt, check_cur_max_cnt())
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
        if i + 1 < n and board[i][j] != board[i + 1][j]:
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            total_max_cnt = max(total_max_cnt, check_cur_max_cnt())
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
print(total_max_cnt)
