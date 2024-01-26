import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
sequence = [int(input()) for _ in range(n)]
stack = []
operators = []
cnt = 1
possible = True
for num in sequence:
    while cnt <= num:
        stack.append(cnt)
        operators.append('+')
        cnt += 1
    if stack[-1] == num:
        stack.pop()
        operators.append('-')
    else:
        possible = False
        break
if possible:
    for op in operators:
        print(op)
else:
    print('NO')
