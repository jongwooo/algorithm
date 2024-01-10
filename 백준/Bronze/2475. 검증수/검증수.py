nums = list(map(int, input().split()))
result = 0
for n in nums:
    result += n ** 2
print(result % 10)
