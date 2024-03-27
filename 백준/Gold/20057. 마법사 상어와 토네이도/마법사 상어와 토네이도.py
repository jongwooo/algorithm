import sys


def tornado_move():
    global r, c, sand_out
    d = 0
    turn = 2
    now = 0
    while (r, c) != (0, 0):
        r += dr[d]
        c += dc[d]
        now += 1
        sand = A[r][c]
        A[r][c] = 0
        left = sand
        for i in range(5):
            for j in range(5):
                scattered_sand = int(sand * proportions[d][i][j])
                left -= scattered_sand
                sr = r + i - 2
                sc = c + j - 2
                if 0 <= sr < N and 0 <= sc < N:
                    A[sr][sc] += scattered_sand
                else:
                    sand_out += scattered_sand
        ar = r + alphas[d][0] - 2
        ac = c + alphas[d][1] - 2
        if 0 <= ar < N and 0 <= ac < N:
            A[ar][ac] += left
        else:
            sand_out += left
        if now == turn // 2 or now == turn:
            d = (d + 1) % 4
            if now == turn:
                now = 0
                turn += 2


def rotate(p):
    return list(reversed(list(zip(*p))))


p0 = [
    [0, 0, 0.02, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.1, 0.07, 0.01, 0],
    [0, 0, 0.02, 0, 0]
]
p1 = rotate(p0)
p2 = rotate(p1)
p3 = rotate(p2)
proportions = (p0, p1, p2, p3)
dr = (0, 1, 0, -1)
dc = (-1, 0, 1, 0)
alphas = ((2, 1), (3, 2), (2, 3), (1, 2))
N = int(sys.stdin.readline())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
r, c = N // 2, N // 2
sand_out = 0
tornado_move()
print(sand_out)
