import sys

t = int(sys.stdin.readline())
yonsei, korea = 0, 0
for _ in range(t):
    yonsei, korea = 0, 0
    for _ in range(9):
        y, k = map(int, sys.stdin.readline().split())
        yonsei += y
        korea += k
    if yonsei < korea:
        print('Korea')
    elif korea < yonsei:
        print('Yonsei')
    else:
        print('Draw')
