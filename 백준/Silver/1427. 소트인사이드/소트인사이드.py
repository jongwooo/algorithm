import sys


nums = [0] * 10
data = list(map(int, list(sys.stdin.readline().rstrip())))
for d in data:
    nums[d] += 1
for i in range(9, -1, -1):
    print(str(i) * nums[i], end='')
