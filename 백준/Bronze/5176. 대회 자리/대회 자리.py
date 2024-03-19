import sys

k = int(sys.stdin.readline())
for _ in range(k):
    p, m = map(int, sys.stdin.readline().split())
    seats = [0] * (m + 1)
    cnt = 0
    for _ in range(p):
        s = int(sys.stdin.readline())
        if seats[s] == 0:
            seats[s] = 1
        else:
            cnt += 1
    print(cnt)
