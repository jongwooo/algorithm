import sys

n = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))
stack = []
idx = 1
for ticket in tickets:
    stack.append(ticket)
    while stack and stack[-1] == idx:
        stack.pop()
        idx += 1
    if len(stack) > 1 and stack[-2] < stack[-1]:
        break
print('Nice' if not stack else 'Sad')
