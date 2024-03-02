import datetime
import sys

m = int(sys.stdin.readline())
d = int(sys.stdin.readline())
special_day = datetime.datetime(2015, 2, 18)
input_day = datetime.datetime(2015, m, d)
if special_day < input_day:
    print('After')
elif special_day > input_day:
    print('Before')
else:
    print('Special')
