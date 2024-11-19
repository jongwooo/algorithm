import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    h, w = map(int, sys.stdin.readline().split())
    grill = []
    for _ in range(h):
        grill.append(sys.stdin.readline().rstrip())
    for now_grill in grill:
        print(now_grill[::-1])
