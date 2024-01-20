from collections import deque

n = int(input())
queue = deque([n])
visited = [0] * (n + 1)
while queue:
    num = queue.popleft()
    if num == 1:
        break
    if num % 3 == 0 and visited[num // 3] == 0:
        queue.append(num // 3)
        visited[num // 3] = visited[num] + 1
    if num % 2 == 0 and visited[num // 2] == 0:
        queue.append(num // 2)
        visited[num // 2] = visited[num] + 1
    if visited[num - 1] == 0:
        queue.append(num - 1)
        visited[num - 1] = visited[num] + 1
print(visited[1])
