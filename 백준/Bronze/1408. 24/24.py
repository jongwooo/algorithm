import sys

h1, m1, s1 = map(int, sys.stdin.readline().split(':'))
h2, m2, s2 = map(int, sys.stdin.readline().split(':'))
h, m = 0, 0
s = s2 - s1
if s < 0:
    s += 60
    m -= 1
m += m2 - m1
if m < 0:
    m += 60
    h -= 1
h += h2 - h1
if h < 0:
    h += 24
print(f'{h:02d}:{m:02d}:{s:02d}')
