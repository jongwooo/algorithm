import sys
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for num in nums:
    print(count_by_range(cards, num, num), end=' ')
