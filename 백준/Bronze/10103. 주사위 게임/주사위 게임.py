import sys

n = int(sys.stdin.readline())
changyeong, sangdeok = 100, 100
for _ in range(n):
    c, s = map(int, sys.stdin.readline().split())
    if c > s:
        sangdeok -= c
    elif c < s:
        changyeong -= s
print(changyeong)
print(sangdeok)
