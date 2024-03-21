import sys

_ = int(sys.stdin.readline())
print(*sorted(list(set(map(int, sys.stdin.readline().split())))))
