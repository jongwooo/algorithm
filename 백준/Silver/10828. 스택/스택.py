import sys


def input():
    return sys.stdin.readline()


n = int(input())
stack = []
for _ in range(n):
    commands = input().split()
    if len(commands) == 2:
        stack.append(int(commands[1]))
    else:
        cmd = commands[0]
        if cmd == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
                stack.pop()
        elif cmd == 'size':
            print(len(stack))
        elif cmd == 'empty':
            print(1 if len(stack) == 0 else 0)
        elif cmd == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[-1])
