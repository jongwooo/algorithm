import sys

t = int(sys.stdin.readline())
a = t // 300
t %= 300
b = t // 60
t %= 60
c = t // 10
t %= 10
if t == 0:
    print(a, b, c)
else:
    print(-1)
