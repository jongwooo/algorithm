import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    print(min(a, b) * 2 - max(a, b))
