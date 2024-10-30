import sys


def dfs(arr, c):
    if len(arr) == m:
        sequences.append(arr)
        return
    back = 0
    for i in range(c, len(nums)):
        if not visited[i] and back != nums[i]:
            visited[i] = 1
            back = nums[i]
            dfs(arr + [nums[i]], i + 1)
            visited[i] = 0


n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [0] * n
sequences = []
dfs([], 0)
for sequence in sequences:
    print(*sequence)
