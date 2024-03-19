import sys

dwarfs = [int(sys.stdin.readline()) for _ in range(9)]
dwarfs_sum = sum(dwarfs)
for i in range(8):
    for j in range(i + 1, 9):
        if dwarfs_sum - dwarfs[i] - dwarfs[j] == 100:
            del dwarfs[j]
            del dwarfs[i]
            for dwarf in dwarfs:
                print(dwarf)
            exit()
