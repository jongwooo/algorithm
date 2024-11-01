import sys

n = int(sys.stdin.readline())
a_win, b_win = 0, 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b < a:
        a_win += 1
    elif a < b:
        b_win += 1
print(a_win, b_win)
