import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sequences = sorted(list(set(i for i in permutations(nums, m))))
for sequence in sequences:
    print(*sequence)
