import sys


def dfs(a, n):
    global min_value
    if a == (N // 2):
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        min_value = min(min_value, abs(start - link))
        return
    else:
        for x in range(n, N):
            visited[x] = True
            dfs(a + 1, x + 1)
            visited[x] = False


N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [False] * N
min_value = 2_000
dfs(0, 0)
print(min_value)
