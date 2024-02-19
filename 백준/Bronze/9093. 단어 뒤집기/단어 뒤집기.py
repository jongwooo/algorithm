import sys

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().rstrip().split(' ')
    for d in data:
        print(d[::-1], end=' ')
