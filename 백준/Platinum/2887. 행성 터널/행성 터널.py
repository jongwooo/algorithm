import sys


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(sys.stdin.readline())
x_list, y_list, z_list = [], [], []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
x_list.sort()
y_list.sort()
z_list.sort()
parent = [i for i in range(n)]
edges = []
for cur in x_list, y_list, z_list:
    for i in range(1, n):
        w1, a = cur[i - 1]
        w2, b = cur[i]
        edges.append((abs(w1 - w2), a, b))
edges.sort()
min_cost = 0
for c, a, b in edges:
    if find(a) != find(b):
        union(a, b)
        min_cost += c
print(min_cost)
