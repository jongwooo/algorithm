import sys

string = list(sys.stdin.readline().rstrip())
boom = list(sys.stdin.readline().rstrip())
boom_size = len(boom)
stack = []
for s in string:
    stack.append(s)
    if stack[len(stack) - boom_size:len(stack)] == boom:
        for _ in range(boom_size):
            stack.pop()
if stack:
    print(*stack, sep='')
else:
    print('FRULA')
