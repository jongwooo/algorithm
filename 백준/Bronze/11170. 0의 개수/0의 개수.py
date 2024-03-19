import sys

t = int(sys.stdin.readline())
for _ in range(t):
    cnt = 0
    n, m = map(int, sys.stdin.readline().split())
    for i in range(n, m + 1):
        cnt += str(i).count('0')
    print(cnt)
