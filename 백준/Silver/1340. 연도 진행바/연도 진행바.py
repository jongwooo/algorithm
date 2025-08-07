import sys

MONTH_NAMES = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
MONTH_DAY_CNT = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month, day, year, time = sys.stdin.readline().split()
day = int(day[:-1])
year = int(year)
hour, minute = map(int, time.split(':'))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    MONTH_DAY_CNT[1] += 1
total_time = sum(MONTH_DAY_CNT) * 24 * 60
last_month_idx = MONTH_NAMES.index(month)
cur_time = (sum(MONTH_DAY_CNT[:last_month_idx]) + day - 1) * 24 * 60 + hour * 60 + minute
print(cur_time / total_time * 100)
