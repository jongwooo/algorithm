import sys


def n_queens(col, i):
    global cnt
    if promising(col, i):
        if i == n:
            cnt += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(col, i + 1)


def promising(col, i):
    k = 1
    flag = True
    while k < i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == (i - k):
            flag = False
            break
        k += 1
    return flag


n = int(sys.stdin.readline())
cnt = 0
col = [0] * (n + 1)
n_queens(col, 0)
print(cnt)
