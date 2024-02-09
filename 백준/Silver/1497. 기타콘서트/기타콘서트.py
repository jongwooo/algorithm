import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
guitars = set()
for _ in range(n):
    name, pos = sys.stdin.readline().split()
    bin_change = ''
    for c in pos:
        if c == 'Y':
            bin_change += '1'
        else:
            bin_change += '0'
    guitars.add(int(bin_change, 2))
guitars -= {0}
if not guitars:
    print(-1)
    exit()
max_cnt = 0
max_guitar = 0
for i in range(1, n + 1):
    for combs in combinations(guitars, i):
        total = 0
        for num in combs:
            total |= num
        cnt = 0
        for j in range(m):
            if total & (1 << j):
                cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            max_guitar = i
print(max_guitar)
