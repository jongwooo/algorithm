import sys

d = int(sys.stdin.readline())
cars = list(map(int, sys.stdin.readline().split()))
cnt = 0
for car in cars:
    if car == d:
        cnt += 1
print(cnt)
