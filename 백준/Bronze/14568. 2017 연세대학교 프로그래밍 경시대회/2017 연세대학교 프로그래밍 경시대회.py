import sys

n = int(sys.stdin.readline())
s = 0
for i in range(2, n - 1, 2):
    s += (n - i - 2) // 2
print(s)
