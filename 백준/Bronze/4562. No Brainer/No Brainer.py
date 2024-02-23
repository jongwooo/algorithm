import sys

t = int(sys.stdin.readline())
for _ in range(t):
    x, y = map(int, sys.stdin.readline().split())
    print(('NO' if x < y else 'MMM') + ' BRAINS')
