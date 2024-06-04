import sys

L = int(sys.stdin.readline())
print(L // 5 if L % 5 == 0 else L // 5 + 1)
