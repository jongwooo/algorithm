import sys

dots = []
n = int(sys.stdin.readline())
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))
dots.append(dots[0])
xr, yr = 0, 0
for i in range(n):
    xr += dots[i][0] * dots[i + 1][1]
    yr += dots[i][1] * dots[i + 1][0]
print(round(abs((xr - yr) / 2), 1))
