import sys


def input():
    return sys.stdin.readline()


def rotate(arr):
    temp = [[0] * m for _ in range(n)]
    loop = min(n, m) // 2
    for i in range(loop):
        for j in range(i, n - i - 1):
            temp[j + 1][i] = arr[j][i]
        for j in range(i, m - i - 1):
            temp[n - i - 1][j + 1] = arr[n - i - 1][j]
        for j in range(n - i - 1, i, -1):
            temp[j - 1][m - i - 1] = arr[j][m - i - 1]
        for j in range(m - i - 1, i, -1):
            temp[i][j - 1] = arr[i][j]
    return temp


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
for _ in range(r):
    arr = rotate(arr)
for a in arr:
    print(*a)
