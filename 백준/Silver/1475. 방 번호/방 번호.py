import sys

nums = [0] * 10
n = int(sys.stdin.readline())
while n > 0:
    i = n % 10
    if i == 6 or i == 9:
        if nums[6] <= nums[9]:
            nums[6] += 1
        else:
            nums[9] += 1
    else:
        nums[i] += 1
    n //= 10
print(max(nums))
