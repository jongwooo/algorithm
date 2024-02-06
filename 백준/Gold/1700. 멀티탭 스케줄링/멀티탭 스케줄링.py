import sys

n, m = map(int, sys.stdin.readline().split())
devices = sys.stdin.readline().rstrip().split()
code = []
cnt = 0
for i in range(m):
    if devices[i] in code:
        continue
    if len(code) < n:
        code.append(devices[i])
        continue
    priority = []
    for c in code:
        if c in devices[i:]:
            priority.append(devices[i:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    code.remove(code[target])
    code.append(devices[i])
    cnt += 1
print(cnt)
