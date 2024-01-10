nums = [int(input()) for _ in range(9)]
max_num = max(nums)
print(f'{max_num}\n{nums.index(max_num) + 1}')
