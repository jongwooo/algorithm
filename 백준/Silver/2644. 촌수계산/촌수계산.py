import sys


def dfs(person, cnt):
    global flag
    visited[person] = True
    if person == b:
        flag = True
        print(cnt)
    for p in family[person]:
        if not visited[p]:
            dfs(p, cnt + 1)


n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
family = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)
flag = False
dfs(a, 0)
if not flag:
    print(-1)
