import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
for _ in range(n):
    commands = sys.stdin.readline().rstrip().split()
    if len(commands) == 2:
        x = int(commands[1])
        if commands[0] == '1':
            queue.appendleft(x)
        if commands[0] == '2':
            queue.append(x)
    else:
        if commands[0] == '3':
            print(-1 if not queue else queue.popleft())
        elif commands[0] == '4':
            print(-1 if not queue else queue.pop())
        elif commands[0] == '5':
            print(len(queue))
        elif commands[0] == '6':
            print(1 if not queue else 0)
        elif commands[0] == '7':
            print(-1 if not queue else queue[0])
        elif commands[0] == '8':
            print(-1 if not queue else queue[-1])
