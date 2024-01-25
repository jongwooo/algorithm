r, c, n = map(int, input().split())
grid = [list(input()) for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
if n <= 1:
    for g in grid:
        print(''.join(g))
elif n % 2 == 0:
    for _ in range(r):
        print('O' * c)
else:
    bombs1 = [['O'] * c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if grid[y][x] == 'O':
                bombs1[y][x] = '.'
            else:
                for i, j in zip(dy, dx):
                    if y + i >= 0 and y + i < r and x + j >= 0 and x + j < c and grid[y + i][x + j] == 'O':
                        bombs1[y][x] = '.'
                        break
    bombs2 = [['O'] * c for i in range(r)]
    for y in range(r):
        for x in range(c):
            if bombs1[y][x] == 'O':
                bombs2[y][x] = '.'
            else:
                for i, j in zip(dy, dx):
                    if y + i >= 0 and y + i < r and x + j >= 0 and x + j < c and bombs1[y + i][x + j] == 'O':
                        bombs2[y][x] = '.'
                        break
    if n % 4 == 3:
        for b1 in bombs1:
            print(''.join(b1))
    if n % 4 == 1:
        for b2 in bombs2:
            print(''.join(b2))
