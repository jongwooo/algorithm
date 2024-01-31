import sys


def input():
    return sys.stdin.readline().rstrip()


def back_tracking(num):
    global ans
    if num > n:
        return
    ans = max(ans, num)
    for i in k:
        back_tracking(num * 10 + i)


n, c = map(int, input().split())
k = list(map(int, input().split()))
ans = 0
back_tracking(0)
print(ans)
