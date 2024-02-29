import sys


def dfs(i, num):
    global add, sub, mul, div, max_num, min_num
    if i == n:
        max_num = max(max_num, num)
        min_num = min(min_num, num)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, num + a[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, num - a[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, num * a[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(num / a[i]))
            div += 1


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
max_num = -(10 ** 9)
min_num = 10 ** 9
dfs(1, a[0])
print(max_num)
print(min_num)
