import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    if len(commands) == 2:
        queue.append(int(commands[1]))
    else:
        if commands[0] == 'pop':
            print(-1 if not queue else queue.popleft())
        elif commands[0] == 'size':
            print(len(queue))
        elif commands[0] == 'empty':
            print(1 if not queue else 0)
        elif commands[0] == 'front':
            print(-1 if not queue else queue[0])
        elif commands[0] == 'back':
            print(-1 if not queue else queue[-1])
