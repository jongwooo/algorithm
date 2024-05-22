import sys

STR, DEX, INT, LUK, n = map(int, sys.stdin.readline().split())
total = STR + DEX + INT + LUK
print((n * 4) - total if total < n * 4 else 0)
