import sys

sw, em, ai, etc = 0, 0, 0, 0
p = int(sys.stdin.readline())
for _ in range(p):
    g, c, n = map(int, sys.stdin.readline().split())
    if g == 1:
        etc += 1
    elif c == 1 or c == 2:
        sw += 1
    elif c == 3:
        em += 1
    else:
        ai += 1
print(sw)
print(em)
print(ai)
print(etc)
