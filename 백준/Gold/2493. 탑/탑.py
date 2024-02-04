import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
stack, result = [], []
for i in range(n):
    while stack:
        if stack[-1][1] > heights[i]:
            result.append(stack[-1][0])
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append((i + 1, heights[i]))
print(*result)
