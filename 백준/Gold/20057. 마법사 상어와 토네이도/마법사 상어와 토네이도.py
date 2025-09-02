import sys


def rotate(p):
    return list(reversed(list(zip(*p))))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def tornado_move():
    global sand_out
    r, c = n // 2, n // 2
    dist = 1
    d = 0
    move = 0
    while True:
        for _ in range(dist):
            dr, dc = dirs[d]
            nr = r + dr
            nc = c + dc
            if (nr, nc) == (0, -1):
                return
            r, c = nr, nc
            sand = a[r][c]
            left = sand
            for i in range(5):
                for j in range(5):
                    scattered_sand = int(sand * proportions[d][i][j])
                    left -= scattered_sand
                    sr = r + i - 2
                    sc = c + j - 2
                    if in_range(sr, sc):
                        a[sr][sc] += scattered_sand
                    else:
                        sand_out += scattered_sand
            ar = r + alphas[d][0] - 2
            ac = c + alphas[d][1] - 2
            if in_range(ar, ac):
                a[ar][ac] += left
            else:
                sand_out += left
        move += 1
        d = (d + 1) % 4
        if move == 2:
            dist += 1
            move = 0


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
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
alphas = ((2, 1), (3, 2), (2, 3), (1, 2))
n = int(sys.stdin.readline())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sand_out = 0
tornado_move()
print(sand_out)
