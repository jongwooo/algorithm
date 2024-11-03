import sys

A, a, B, b, P = map(int, sys.stdin.readline().split())
if A > P or B > P:
    print('No')
elif A + B <= P:
    print('Yes')
elif a >= B:
    print('Yes')
elif b >= A:
    print('Yes')
else:
    print('No')
