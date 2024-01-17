n = int(input())
m = int(input())
board = [[0] * n for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
y = n // 2
x = n // 2
board[y][x] = 1
num = 2
i = 0
repeat = 1
m_y, m_x = y + 1, x + 1
while y != 0 or x != 0:
    flag = 0
    for _ in range(2):
        for _ in range(repeat):
            y += dy[i]
            x += dx[i]
            board[y][x] = num
            if num == m:
                m_y, m_x = y + 1, x + 1
            if y == 0 and x == 0:
                flag = 1
                break
            num += 1
        if flag == 1:
            break
        i = (i + 1) % 4
    repeat += 1

for b in board:
    print(*b)
print(m_y, m_x)
