import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
stack = []
result = [-1] * n
for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        result[stack.pop()] = a[i]
    stack.append(i)
print(*result)
