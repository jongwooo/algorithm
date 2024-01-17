def star(n, y, x):
    length = 4 * n - 3
    if length == 1:
        board[y][x] = '*'
        return
    else:
        for i in range(length):
            board[y + i][x] = '*'
            board[y][x + i]= '*'
            board[y + length - 1][x + i] = '*'
            board[y + i][x + length -1] = '*'
        n -= 1
        y += 2
        x += 2
        star(n, y, x)
        return


n = int(input())
length = 4 * n - 3
board = [[' '] * length for _ in range(length)]
star(n, 0, 0)
for i in range(length):
    print(*board[i], sep='')
