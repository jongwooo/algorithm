import sys

max_passenger = 0
passenger = 0
for _ in range(10):
    off, on = map(int, sys.stdin.readline().split())
    passenger -= off
    passenger += on
    max_passenger = max(max_passenger, passenger)
print(max_passenger)
