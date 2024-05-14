import sys

n = int(sys.stdin.readline())
a = [0] + list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]
for query in queries:
    if query[0] == 1:
        l, r, k = query[1:]
        print(a[l:r + 1].count(k))
    else:
        l, r = query[1:]
        for i in range(l, r + 1):
            a[i] = 0
