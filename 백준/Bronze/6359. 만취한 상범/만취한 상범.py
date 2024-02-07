import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    rooms = [0] * n
    for r in range(1, n + 1):
        for i in range(n):
            if (i + 1) % r == 0:
                rooms[i] = 1 - rooms[i]
    cnt = 0
    for room_open in rooms:
        if room_open == 1:
            cnt += 1
    print(cnt)
