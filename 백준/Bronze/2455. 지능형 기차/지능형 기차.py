import sys

max_passenger = 0
cur = 0
for _ in range(4):
    off, on = map(int, sys.stdin.readline().split())
    cur -= off
    cur += on
    max_passenger = max(max_passenger, cur)
print(max_passenger)
