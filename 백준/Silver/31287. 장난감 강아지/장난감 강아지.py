import sys

n, k = map(int, sys.stdin.readline().split())
s = sys.stdin.readline()
if k > (n >> 1):
    k = (n >> 1)
cur_y, cur_x = 0, 0
while k:
    for c in s:
        if c == 'U':
            cur_y += 1
        elif c == 'D':
            cur_y -= 1
        elif c == 'L':
            cur_x -= 1
        elif c == 'R':
            cur_x += 1
        if cur_y == 0 and cur_x == 0:
            print('YES')
            exit(0)
    k -= 1
print('NO')
