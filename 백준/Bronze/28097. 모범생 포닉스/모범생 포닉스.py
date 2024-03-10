import sys

n = int(sys.stdin.readline())
t = sum(list(map(int, sys.stdin.readline().split()))) + 8 * (n - 1)
print(t // 24, t % 24)
