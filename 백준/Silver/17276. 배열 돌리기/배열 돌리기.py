import sys

input = sys.stdin.readline

for _ in range(int(input())):
    n, d = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(n)]
    temp = [item[:] for item in arr]
    x_origin = [(0, 0), (0, n // 2), (0, n - 1), (n // 2, n - 1), (n - 1, n - 1), (n - 1, n // 2), (n - 1, 0),
                (n // 2, 0)]
    dx_origin = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
    cnt = d // 45
    if cnt < 0:
        x_origin = list(reversed(x_origin))
        dx_origin = list(reversed(dx_origin))
    for _ in range(abs(cnt)):
        x = x_origin[:]
        dx = dx_origin[:]
        for j in range(n // 2):
            for k in range(8):
                px, py = x[k]
                nx, ny = x[k + 1] if k < 7 else x[0]
                temp[nx][ny] = arr[px][py]
            x = [(x[i][0] + dx[i][0], x[i][1] + dx[i][1]) for i in range(8)]
            arr = [item[:] for item in temp]
    for line in arr:
        print(*line, sep=' ')
