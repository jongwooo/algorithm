import sys

n = int(sys.stdin.readline())
friends = [list(sys.stdin.readline()) for _ in range(n)]
graph = [[0] * n for _ in range(n)]
for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if friends[a][b] == 'Y' or (friends[a][k] == friends[k][b] == 'Y'):
                graph[a][b] = 1
max_2_friends_cnt = 0
for g in graph:
    if max_2_friends_cnt < sum(g):
        max_2_friends_cnt = sum(g)
print(max_2_friends_cnt)
