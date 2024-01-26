import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
queue = deque()
commands = {
    'pop': lambda: print(-1) if not queue else print(queue.popleft()),
    'size': lambda: print(len(queue)),
    'empty': lambda: print(1) if not queue else print(0),
    'front': lambda: print(-1) if not queue else print(queue[0]),
    'back': lambda: print(-1) if not queue else print(queue[-1]),
}

for _ in range(n):
    command = input().split()
    if command[0] == 'push':
        queue.append(int(command[1]))
    else:
        commands[command[0]]()
