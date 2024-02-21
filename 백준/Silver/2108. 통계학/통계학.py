import sys

n = int(sys.stdin.readline())
nums = sorted([int(sys.stdin.readline()) for _ in range(n)])
cnt = dict()
for num in nums:
    if num not in cnt:
        cnt[num] = 1
    else:
        cnt[num] += 1
print(round(sum(nums) / n))
print(nums[n // 2])
freq = max(cnt.values())
freq_nums = []
for k, v in cnt.items():
    if v == freq:
        freq_nums.append(k)
print(freq_nums[0] if len(freq_nums) == 1 else sorted(freq_nums)[1])
print(nums[-1] - nums[0])
