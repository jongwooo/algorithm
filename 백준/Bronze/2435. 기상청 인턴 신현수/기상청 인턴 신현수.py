import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
result = []
for i in range(0, n - k + 1):
    result.append(sum(nums[i:i + k]))
print(max(result))
