import sys
import itertools

dwarfs = sorted([int(sys.stdin.readline()) for _ in range(9)])
for some_dwarf in itertools.combinations(dwarfs, 7):
    if sum(some_dwarf) == 100:
        for dwarf in some_dwarf:
            print(dwarf)
        break
