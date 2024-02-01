import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
nums = [(i + 1) for i in range(n)]
sequences = [i for i in combinations_with_replacement(nums, m)]
for sequence in sequences:
    print(*sequence)
