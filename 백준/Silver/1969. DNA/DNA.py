import sys


def input():
    return sys.stdin.readline()


n, m = map(int, input().split())
data = [input() for _ in range(n)]
dna = ''
dist = 0
for i in range(m):
    dic = {}
    for d in data:
        if d[i] not in dic:
            dic[d[i]] = 1
        else:
            dic[d[i]] += 1
    arr = list(dic.items())
    arr.sort(key=lambda x: (-x[1], x[0]))
    dna += arr[0][0]
    dist += n - arr[0][1]
print(dna)
print(dist)
