import sys
from datetime import date

today = list(map(int, sys.stdin.readline().split()))
d_day = list(map(int, sys.stdin.readline().split()))
if today[0] + 1_000 < d_day[0]:
    print('gg')
elif today[0] + 1_000 == d_day[0] and (today[1], today[2]) <= (d_day[1], d_day[2]):
    print('gg')
else:
    today = date(*today)
    d_day = date(*d_day)
    print(f'D{today.toordinal() - d_day.toordinal()}')
