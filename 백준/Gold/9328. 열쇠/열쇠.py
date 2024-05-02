import sys
from collections import deque


def open_doors_using_existing_keys():
    global doors, building
    for key in keys:
        if key == '0':
            break
        doors[ord(key) - 97] = True
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if building[i][j].isupper() and doors[ord(building[i][j].lower()) - 97]:
                building[i][j] = '.'


def bfs():
    global building, keys
    cnt = 0
    queue = deque([(0, 0)])
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-1, 0), (0, 1), (0, -1), (1, 0)):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < h + 2 and 0 <= ny < w + 2 and not visited[nx][ny] and building[nx][ny] != '*':
                if building[nx][ny].isupper():
                    if doors[ord(building[nx][ny].lower()) - 97]:
                        building[nx][ny] = '.'
                    else:
                        continue
                elif building[nx][ny].islower():
                    doors[ord(building[nx][ny]) - 97] = True
                    building[nx][ny] = '.'
                    visited = [[False] * (w + 2) for _ in range(h + 2)]
                    queue = deque([])
                elif building[nx][ny] == '$':
                    building[nx][ny] = '.'
                    cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    return cnt


t = int(sys.stdin.readline())
for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())
    building = [['.'] * (w + 2)] + [list('.' + sys.stdin.readline().rstrip() + '.') for _ in range(h)] + [
        ['.'] * (w + 2)]
    keys = list(sys.stdin.readline().rstrip())
    doors = [False] * 26
    open_doors_using_existing_keys()
    print(bfs())
