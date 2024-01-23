import sys

input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
p = 0
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a[(p + query[1] - 1) % n] += query[2]
    elif query[0] == 2:
        p -= query[1]
    else:
        p += query[1]
for i in range(p, p + n):
    print(a[i % n], end=' ')
