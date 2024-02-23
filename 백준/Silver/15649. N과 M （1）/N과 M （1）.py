import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
for sequence in permutations([(i + 1) for i in range(n)], m):
    print(*sequence)
