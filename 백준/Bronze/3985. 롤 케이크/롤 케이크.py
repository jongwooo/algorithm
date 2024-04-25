import sys

L = int(sys.stdin.readline())
N = int(sys.stdin.readline())
li = list()
d = dict()
for guest in range(1, N + 1):
    p, k = map(int, sys.stdin.readline().split())
    li.append(k - p)
    for i in range(p, k + 1):
        if i in list(d.keys()):
            continue
        d[i] = guest
print(li.index(max(li)) + 1)
result = list()
for guest in range(1, N + 1):
    result.append(list(d.values()).count(guest))
print(result.index(max(result)) + 1)
