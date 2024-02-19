import sys

n = int(sys.stdin.readline())
coordinates = []
for _ in range(n):
    xi, yi = map(int, sys.stdin.readline().split())
    coordinates.append((xi, yi))
coordinates.sort(key=lambda x: (x[0], x[1]))
for c in coordinates:
    print(*c)
