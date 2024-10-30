import sys


def lotto(nums, c):
    if len(nums) == 6:
        print(*nums)
        return
    for i in range(c, len(s)):
        lotto(nums + [s[i]], i + 1)

while True:
    k, *s = map(int, sys.stdin.readline().split())
    if k == 0:
        break
    lotto([], 0)
    print()
