import sys

n = int(sys.stdin.readline())
nums = [sys.stdin.readline().rstrip() for _ in range(n)]
k = int(sys.stdin.readline())
base36 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
base36_diff = []
num_sep = []
num_sum = 0
for num in nums:
    num_sep.append(list(num))
    num_sum += int(num, 36)
for b in base36:
    num_sum_diff = 0
    for num in num_sep:
        temp = ''
        for n in num:
            if n == b:
                temp += 'Z'
            else:
                temp += n
        num_sum_diff += int(temp, 36)
    base36_diff.append(num_sum_diff - num_sum)
max_sum = num_sum + sum(sorted(base36_diff, reverse=True)[:k])
result = ''
while max_sum > 0:
    result += base36[max_sum % 36]
    max_sum //= 36
print(result[::-1] if result else '0')
