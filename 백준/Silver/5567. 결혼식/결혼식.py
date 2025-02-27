import sys
from collections import deque


def bfs():
    queue = deque([1])
    visited[1] = 1
    while queue:
        friend_num = queue.popleft()
        for person_num in graph[friend_num]:
            if not visited[person_num]:
                queue.append(person_num)
                visited[person_num] = visited[friend_num] + 1


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
bfs()
result = 0
for i in range(2, n + 1):
    if 0 < visited[i] <= 3:
        result += 1
print(result)
