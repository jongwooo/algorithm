import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
cnt = n * m
for i in range(n - 7):
    for j in range(m - 7):
        w, b = 0, 0
        for col in range(i, i + 8):
            for row in range(j, j + 8):
                if (col + row) % 2 == 0:
                    if board[col][row] != 'W':
                        w += 1
                    else:
                        b += 1
                else:
                    if board[col][row] != 'W':
                        b += 1
                    else:
                        w += 1
        cnt = min(cnt, min(w, b))
print(cnt)
