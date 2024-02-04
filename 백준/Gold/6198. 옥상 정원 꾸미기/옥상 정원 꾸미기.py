import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
cnt = 0
for h in heights:
    while stack and stack[-1] <= h:
        stack.pop()
    stack.append(h)
    cnt += len(stack) - 1
print(cnt)
