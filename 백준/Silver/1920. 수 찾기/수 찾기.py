import sys


def binary(l, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if l == a[mid]:
        return 1
    elif l < a[mid]:
        return binary(l, start, mid - 1)
    else:
        return binary(l, mid + 1, end)


n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for num in nums:
    print(binary(num, 0, n - 1))
