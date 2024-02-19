import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    commands = sys.stdin.readline().split()
    if len(commands) == 2:
        stack.append(int(commands[1]))
    else:
        if commands[0] == '2':
            print(-1 if not stack else stack.pop())
        elif commands[0] == '3':
            print(len(stack))
        elif commands[0] == '4':
            print(1 if not stack else 0)
        elif commands[0] == '5':
            print(-1 if not stack else stack[-1])
