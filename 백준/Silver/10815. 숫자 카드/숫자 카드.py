import bisect
import sys

n = int(sys.stdin.readline())
cards = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
for num in nums:
    print(1 if cards[bisect.bisect(cards, num) - 1] == num else 0, end=' ')
