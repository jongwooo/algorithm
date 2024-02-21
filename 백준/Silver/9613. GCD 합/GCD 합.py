import sys


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(sys.stdin.readline())
for _ in range(t):
    nums = list(map(int, sys.stdin.readline().split()))
    total = 0
    for i in range(1, len(nums)):
        for j in range(i + 1, len(nums)):
            total += gcd(nums[i], nums[j])
    print(total)
