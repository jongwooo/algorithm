import sys

nums = [(i + 1) for i in range(20)]
for _ in range(10):
    i, j = map(int, sys.stdin.readline().split())
    temp = nums[i - 1:j]
    nums[i - 1:j] = temp[::-1]
print(*nums)
