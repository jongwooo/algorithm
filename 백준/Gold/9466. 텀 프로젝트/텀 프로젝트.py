import sys

sys.setrecursionlimit(10 ** 9)


def dfs(x, cycle):
    global success
    visited[x] = True
    cycle.append(x)
    next_x = choose[x]
    if visited[next_x]:
        if next_x in cycle:
            success += cycle[cycle.index(next_x):]
    else:
        dfs(next_x, cycle)


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    choose = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [False] * (n + 1)
    success = []
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, [])
    print(n - len(success))
