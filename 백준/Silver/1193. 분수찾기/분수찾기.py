import sys

x = int(sys.stdin.readline())
row = 1
while x > row:
    x -= row
    row += 1
a = x
b = row - x + 1
print(f'{a}/{b}' if row % 2 == 0 else f'{b}/{a}')
