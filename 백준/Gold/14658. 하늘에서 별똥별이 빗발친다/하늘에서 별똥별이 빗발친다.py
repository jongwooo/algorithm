import sys

N, M, L, K = map(int, sys.stdin.readline().split())
shooting_stars = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
max_cnt = 0
for fx, fy in shooting_stars:
    for sx, sy in shooting_stars:
        hit_cnt = 0
        for px, py in shooting_stars:
            if fx <= px <= fx + L and sy <= py <= sy + L:
                hit_cnt += 1
        max_cnt = max(max_cnt, hit_cnt)
print(K - max_cnt)
