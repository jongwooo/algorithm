import sys
from itertools import permutations


def input():
    return sys.stdin.readline()


data = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
nums = list(permutations(data, 3))
n = int(input())
for _ in range(n):
    num, strike, ball = map(int, input().split())
    num = list(str(num))
    rmcnt = 0
    for i in range(len(nums)):
        s = b = 0
        i -= rmcnt
        for j in range(3):
            if nums[i][j] == num[j]:
                s += 1
            elif num[j] in nums[i]:
                b += 1
        if strike != s or ball != b:
            nums.remove(nums[i])
            rmcnt += 1
print(len(nums))
