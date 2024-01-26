import sys


def input():
    return sys.stdin.readline().rstrip()


n, kim, lim = map(int, input().split())
cnt = 0
while kim != lim:
    kim -= kim // 2
    lim -= lim // 2
    cnt += 1
print(cnt)
