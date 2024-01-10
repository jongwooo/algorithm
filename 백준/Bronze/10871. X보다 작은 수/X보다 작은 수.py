n, x = map(int, input().split())
nums = list(map(int, input().split()))
for i in range(n):
    if nums[i] < x:
        print(nums[i], end=' ')
