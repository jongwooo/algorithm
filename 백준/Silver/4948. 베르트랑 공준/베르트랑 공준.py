import sys


nums = [1 for i in range(123_456 * 2 + 1)]
for i in range(1, 123_456 * 2 + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            nums[i] = 0
            break

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        cnt += nums[i]
    print(cnt)
