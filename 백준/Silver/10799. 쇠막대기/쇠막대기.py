import sys


def input():
    return sys.stdin.readline().rstrip()


data = input()
stack = []
cnt = 0
for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
    elif data[i - 1] == '(':
        stack.pop()
        cnt += len(stack)
    else:
        stack.pop()
        cnt += 1
print(cnt)
