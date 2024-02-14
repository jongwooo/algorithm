import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    shop = list(map(int, sys.stdin.readline().split()))
    print(2 * (max(shop) - min(shop)))
