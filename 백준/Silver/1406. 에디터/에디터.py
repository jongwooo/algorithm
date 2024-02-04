import sys

string = list(sys.stdin.readline().rstrip())
stack = []
m = int(sys.stdin.readline())
for _ in range(m):
    commands = list(sys.stdin.readline().split())
    if commands[0] == 'L':
        if string:
            stack.append(string.pop())
    elif commands[0] == 'D':
        if stack:
            string.append(stack.pop())
    elif commands[0] == 'B':
        if string:
            string.pop()
    elif commands[0] == 'P':
        string.append(commands[1])
string.extend(reversed(stack))
print(''.join(string))
