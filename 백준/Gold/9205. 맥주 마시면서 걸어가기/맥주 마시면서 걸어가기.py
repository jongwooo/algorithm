import sys
from collections import deque


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def bfs():
    if distance(home, festival) <= 1_000:
        visited[n] = True
        return
    queue = deque([])
    for i, cvs_i in enumerate(cvs):
        if distance(home, cvs_i) <= 1_000:
            queue.append(cvs_i)
            visited[i] = True
    while queue:
        x, y = queue.popleft()
        for i, cvs_i in enumerate(cvs):
            if distance((x, y), cvs_i) <= 1_000 and not visited[i]:
                queue.append(cvs_i)
                visited[i] = True


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cvs = []
    home = tuple(map(int, sys.stdin.readline().split()))
    for _ in range(n):
        cvs.append(tuple(map(int, sys.stdin.readline().split())))
    festival = tuple(map(int, sys.stdin.readline().split()))
    cvs.append(festival)
    visited = [False] * (n + 1)
    bfs()
    print('happy' if visited[n] else 'sad')
