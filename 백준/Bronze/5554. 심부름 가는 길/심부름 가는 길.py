import sys

time = 0
for _ in range(4):
    time += int(sys.stdin.readline())
print(time // 60)
print(time % 60)
