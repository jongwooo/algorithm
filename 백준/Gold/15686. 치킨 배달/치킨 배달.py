import sys


def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


def dfs(idx, chosen):
    global min_dist
    if len(chosen) == m:
        dist = 0
        for hr, hc in homes:
            temp_dist = INF
            for cr, cc in chosen:
                temp_dist = min(temp_dist, distance(hr, hc, cr, cc))
            dist += temp_dist
        min_dist = min(min_dist, dist)
        return
    for i in range(idx, len(chicken_restaurants)):
        dfs(i + 1, chosen + [chicken_restaurants[i]])


INF = int(1e9)
HOME = 1
CHICKEN_RESTAURANT = 2
n, m = map(int, sys.stdin.readline().split())
chicken_restaurants = []
homes = []
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(n):
        if temp[j] == CHICKEN_RESTAURANT:
            chicken_restaurants.append((i, j))
        elif temp[j] == HOME:
            homes.append((i, j))
min_dist = INF
dfs(0, [])
print(min_dist)
