import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
queue = deque([])
command_dict = {
    'push_front': queue.appendleft,
    'push_back': queue.append,
    'pop_front': lambda: -1 if not queue else queue.popleft(),
    'pop_back': lambda: -1 if not queue else queue.pop(),
    'size': lambda: len(queue),
    'empty': lambda: 1 if not queue else 0,
    'front': lambda: -1 if not queue else queue[0],
    'back': lambda: -1 if not queue else queue[-1],
}
for _ in range(n):
    commands = input().split()
    cmd = commands[0]
    if cmd in ['push_front', 'push_back']:
        command_dict[cmd](commands[1])
    else:
        print(command_dict[cmd]())
