import sys


def input():
    return sys.stdin.readline()


n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
max_sum = 0
for i in range(m - 2):
    for j in range(i + 1, m - 1):
        for k in range(j + 1, m):
            s = 0
            for d in data:
                s += max(max(d[i], d[j]), d[k])
            max_sum = max(max_sum, s)
print(max_sum)
