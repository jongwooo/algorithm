import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
rooms = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    for room in range(x, y):
        rooms[room] = 1
print(rooms.count(0) - 1)
