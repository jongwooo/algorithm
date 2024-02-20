import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
f = [0] * 1_000_001
for i in a:
    f[i] += 1
ngf = [-1] * n
stack = []
for i in range(n):
    while stack and f[a[stack[-1]]] < f[a[i]]:
        ngf[stack.pop()] = a[i]
    stack.append(i)
print(*ngf)
