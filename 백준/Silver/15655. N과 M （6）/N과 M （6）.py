import sys


def combinations(arr, c):
    if len(arr) == m:
        sequences.append(arr)
        return
    for i in range(c, len(nums)):
        combinations(arr + [nums[i]], i + 1)


n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
sequences = []
combinations([], 0)
for sequence in sequences:
    print(*sequence)
