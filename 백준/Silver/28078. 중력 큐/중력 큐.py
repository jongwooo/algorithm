import sys
from collections import deque

q = int(sys.stdin.readline())
queue = deque([])
d = 0
b, w = 0, 0
for _ in range(q):
    cmd = sys.stdin.readline().rstrip()
    if cmd == 'pop':
        if len(queue) != 0:
            popped = queue.popleft()
            if popped == 0:
                b -= 1
            elif popped == -1:
                w -= 1
    else:
        c, o = cmd.split()
        if c == 'push':
            if o == 'b':
                queue.append(0)
                b += 1
            if o == 'w':
                queue.append(-1)
                w += 1
        elif c == 'rotate':
            if o == 'l':
                d = (d - 1) % 4
            elif o == 'r':
                d = (d + 1) % 4
        elif c == 'count':
            if o == 'b':
                print(b)
            elif o == 'w':
                print(w)
    if d == 1:
        while queue and queue[0] != -1:
            queue.popleft()
            b -= 1
    elif d == 3:
        while queue and queue[-1] != -1:
            queue.pop()
            b -= 1
