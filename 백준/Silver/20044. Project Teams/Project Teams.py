import sys

n = int(sys.stdin.readline())
s = sorted(list(map(int, sys.stdin.readline().split())))
arr = []
for i in range(n):
    arr.append(s[i] + s[2 * n - i - 1])
print(min(arr))
