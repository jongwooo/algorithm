import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
y, m = 0, 0
for t in times:
    y += (t // 30 + 1) * 10
    m += (t // 60 + 1) * 15
if y < m:
    print('Y', y)
elif m < y:
    print('M', m)
else:
    print('Y M', y)
