import sys

INF = int(1e9)


def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def dfs(idx, chosen):
    global min_dist
    if len(chosen) == m:
        dist = 0
        for hx, hy in homes:
            temp_dist = INF
            for cx, cy in chosen:
                temp_dist = min(temp_dist, distance(hx, hy, cx, cy))
            dist += temp_dist
        min_dist = min(min_dist, dist)
        return
    for i in range(idx, len(chicken_restaurants)):
        dfs(i + 1, chosen + [chicken_restaurants[i]])


n, m = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken_restaurants = []
homes = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            chicken_restaurants.append((i, j))
        elif grid[i][j] == 1:
            homes.append((i, j))
min_dist = INF
dfs(0, [])
print(min_dist)
