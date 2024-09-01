import sys

a, b = map(int, sys.stdin.readline().split())
k, x = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(k - x, k + x + 1):
    if a <= i <= b:
        cnt += 1
print('IMPOSSIBLE' if cnt == 0 else cnt)
