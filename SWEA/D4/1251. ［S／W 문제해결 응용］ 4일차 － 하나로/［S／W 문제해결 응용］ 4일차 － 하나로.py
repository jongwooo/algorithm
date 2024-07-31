def find(i):
    global parent
    if parent[i] != i:
        parent[i] = find(parent[i])
    return parent[i]


def union(a, b):
    global parent
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    parent = [i for i in range(N)]
    edges = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            edges.append(((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2, i, j))
    edges.sort()
    min_cost = 0.0
    for edge in edges:
        L, i, j = edge
        if find(i) != find(j):
            union(i, j)
            min_cost += L
    print(f'#{test_case} {round(min_cost * E)}')
