import sys

L, P = map(int, sys.stdin.readline().split())
news = list(map(int, sys.stdin.readline().split()))
for i in news:
    print(i - L * P, end=' ')
