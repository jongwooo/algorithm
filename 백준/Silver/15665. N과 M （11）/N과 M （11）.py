import sys


def dfs(arr):
    if len(arr) == m:
        sequences.append(arr)
        return
    back = 0
    for i in range(len(nums)):
        if back != nums[i]:
            back = nums[i]
            dfs(arr + [nums[i]])


n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0] * n
sequences = []
dfs([])
for sequence in sequences:
    print(*sequence)
