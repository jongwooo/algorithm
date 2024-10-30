import sys


def products(arr):
    if len(arr) == m:
        sequences.append(arr)
        return
    for i in range(len(nums)):
        products(arr + [nums[i]])


n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
sequences = []
products([])
for sequence in sequences:
    print(*sequence)
