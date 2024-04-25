import sys

n, m = map(int, sys.stdin.readline().split())
if m == 1 or m == 2:
    print('NEWBIE!')
elif m <= n:
    print('OLDBIE!')
else:
    print('TLE!')
