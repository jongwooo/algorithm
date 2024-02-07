import sys

nums = [0] * 1001
sum_nums = 0
for _ in range(10):
    num = int(sys.stdin.readline())
    sum_nums += num
    nums[num] += 1
print(sum_nums // 10)
print(nums.index(max(nums)))
