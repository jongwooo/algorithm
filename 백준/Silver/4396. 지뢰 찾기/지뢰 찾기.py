n = int(input())
mine = [list(input()) for _ in range(n)]
board = [list(input()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for y in range(n):
    for x in range(n):
        if board[y][x] == '.':
            continue
        if mine[y][x] == '.':
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if mine[ny][nx] == '*':
                    cnt += 1
            result[y][x] = str(cnt)
        elif mine[y][x] == '*':
            for col in range(n):
                for row in range(n):
                    if mine[col][row] == '*':
                        result[col][row] = '*'

for col in range(n):
    for row in range(n):
        print(result[col][row], end='')
    print()
