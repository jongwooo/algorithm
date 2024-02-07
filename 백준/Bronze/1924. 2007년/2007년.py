import sys

day_of_week = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN'
}
months = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
x, y = map(int, sys.stdin.readline().split())
day = 0
while x > 1:
    x -= 1
    day += months[x]
day += y - 1
print(day_of_week[day % 7])
