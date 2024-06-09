import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
atk = a[0]
a = sorted(a[1:])
flag = True
for ai in a:
    if atk > ai:
        atk += ai
    else:
        flag = False
        break
print('Yes' if flag else 'No')
