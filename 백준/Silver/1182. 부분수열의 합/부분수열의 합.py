import sys


def dfs(idx, num):
    global cnt
    if n <= idx:
        return
    num += nums[idx]
    if num == s:
        cnt += 1
    dfs(idx + 1, num)
    dfs(idx + 1, num - nums[idx])


n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
cnt = 0
dfs(0, 0)
print(cnt)
