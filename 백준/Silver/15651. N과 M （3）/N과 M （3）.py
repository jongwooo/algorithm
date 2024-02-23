import sys


def dfs():
    if len(seq) == m:
        print(' '.join(map(str, seq)))
        return
    for i in range(1, n + 1):
        seq.append(i)
        dfs()
        seq.pop()


n, m = map(int, sys.stdin.readline().split())
seq = []
dfs()
