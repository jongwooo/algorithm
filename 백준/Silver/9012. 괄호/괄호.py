import sys


def input():
    return sys.stdin.readline().rstrip()


t = int(input())
for _ in range(t):
    parenthesis = list(input())
    cnt = 0
    for p in parenthesis:
        if p == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            break
    print('YES' if cnt == 0 else 'NO')
