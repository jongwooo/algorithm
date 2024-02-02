import sys


def input():
    return sys.stdin.readline()


t = int(input())
for _ in range(t):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        cx, cy, cr = map(int, input().split())
        dis1 = (x1 - cx) ** 2 + (y1 - cy) ** 2
        dis2 = (x2 - cx) ** 2 + (y2 - cy) ** 2
        pow_cr = cr ** 2
        if pow_cr > dis1 and pow_cr > dis2:
            continue
        elif pow_cr > dis1:
            cnt += 1
        elif pow_cr > dis2:
            cnt += 1
    print(cnt)
