import sys

t = int(sys.stdin.readline())
for _ in range(t):
    points = sorted(list(map(int, sys.stdin.readline().split())))[1:-1]
    print(sum(points) if points[-1] < points[0] + 4 else 'KIN')
