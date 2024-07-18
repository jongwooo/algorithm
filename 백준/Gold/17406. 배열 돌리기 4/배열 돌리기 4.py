import sys
from collections import deque
from copy import deepcopy


def dfs(cnt):
    global visited, min_value
    if cnt == k:
        copied = deepcopy(a)
        for r, c, s in queue:
            rotate(copied, r, c, s)
        min_value = min(min_value, calculate_value(copied))
        return
    for i in range(k):
        if not visited[i]:
            visited[i] = 1
            queue.append(rotate_commands[i])
            dfs(cnt + 1)
            visited[i] = 0
            queue.pop()


def rotate(arr, r, c, s):
    for j in range(1, s + 1):
        temp = arr[r - j][c + j]
        for i in range(2 * j):
            arr[r - j][c + j - i] = arr[r - j][c + j - i - 1]
        for i in range(2 * j):
            arr[r - j + i][c - j] = arr[r - j + i + 1][c - j]
        for i in range(2 * j):
            arr[r + j][c - j + i] = arr[r + j][c - j + i + 1]
        for i in range(2 * j - 1):
            arr[r + j - i][c + j] = arr[r + j - i - 1][c + j]
        arr[r - j + 1][c + j] = temp


def calculate_value(arr):
    value = sys.maxsize
    for i in arr:
        value = min(value, sum(i))
    return value


n, m, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
min_value = sys.maxsize
rotate_commands = []
for _ in range(k):
    r, c, s = map(int, sys.stdin.readline().split())
    rotate_commands.append((r - 1, c - 1, s))
visited = [0] * k
queue = deque([])
dfs(0)
print(min_value)
