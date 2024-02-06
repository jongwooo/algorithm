import sys

n = int(sys.stdin.readline())
points = list(map(int, sys.stdin.readline().split()))
total = 0
temp = 0
for point in points:
    if point == 1:
        temp += point
    else:
        total += temp * (temp + 1) // 2
        temp = 0
if temp != 0:
    total += temp * (temp + 1) // 2
print(total)
