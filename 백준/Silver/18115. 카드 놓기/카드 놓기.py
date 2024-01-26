import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
commands = list(map(int, input().split()))
commands.reverse()
queue = deque([])
for i in range(n):
    if commands[i] == 1:
        queue.appendleft(i + 1)
    elif commands[i] == 2:
        queue.insert(1, i + 1)
    elif commands[i] == 3:
        queue.append(i + 1)
print(*queue)
