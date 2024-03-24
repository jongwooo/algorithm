import sys

N, Q = map(int, sys.stdin.readline().split())
money = [0] * (N + 1)
for _ in range(Q):
    query, p, q = map(int, sys.stdin.readline().split())
    if query == 1:
        money[p] += q
    else:
        print(sum(money[p:q + 1]))
