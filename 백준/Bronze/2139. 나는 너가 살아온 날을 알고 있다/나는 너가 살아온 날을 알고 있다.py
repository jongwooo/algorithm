import sys
from datetime import datetime

while True:
    d, m, y = map(int, sys.stdin.readline().split())
    if d == m == y == 0:
        break
    period = datetime(year=y, month=m, day=d) - datetime(year=y, month=1, day=1)
    print(period.days + 1)
