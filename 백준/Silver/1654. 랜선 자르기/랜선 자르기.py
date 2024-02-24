import sys


def binary(low, high):
    if high < low:
        return
    global n
    global result
    mid = (low + high) // 2
    temp = 0
    for i in cables:
        temp += i // mid
    if temp >= n:
        result = mid
        binary(mid + 1, high)
    else:
        binary(low, mid - 1)


k, n = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline()) for _ in range(k)]
standard = max(cables)
result = 0
binary(0, standard * 2)
print(result)
