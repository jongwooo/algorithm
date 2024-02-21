import sys


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr) + 1) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    sorted_arr = []
    low = high = 0
    while low < len(low_arr) and high < len(high_arr):
        if low_arr[low] <= high_arr[high]:
            sorted_arr.append(low_arr[low])
            result.append(low_arr[low])
            low += 1
        else:
            sorted_arr.append(high_arr[high])
            result.append(high_arr[high])
            high += 1
    while low < len(low_arr):
        sorted_arr.append(low_arr[low])
        result.append(low_arr[low])
        low += 1
    while high < len(high_arr):
        sorted_arr.append(high_arr[high])
        result.append(high_arr[high])
        high += 1
    return sorted_arr


result = []
n, k = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
merge_sort(arr)
print(result[k - 1] if k <= len(result) else -1)
