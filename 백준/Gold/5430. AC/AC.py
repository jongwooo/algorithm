import sys
from collections import deque

t = int(sys.stdin.readline())
for _ in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    if n == 0:
        x = deque()
    err = False
    rev = 0
    for func in p:
        if func == 'R':
            rev += 1
        elif func == 'D':
            if x:
                if rev % 2 == 0:
                    x.popleft()
                else:
                    x.pop()
            else:
                err = True
                break
    if rev % 2 == 1:
        x.reverse()
    print('error' if err else f'[{",".join(x)}]')
