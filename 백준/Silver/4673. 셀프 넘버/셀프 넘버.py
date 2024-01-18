def d(n):
    return n + sum(map(int, str(n)))


nums = list(range(1, 10001))
for i in range(1, 10001):
    if d(i) in nums:
        nums.remove(d(i))
for num in nums:
    print(num)
