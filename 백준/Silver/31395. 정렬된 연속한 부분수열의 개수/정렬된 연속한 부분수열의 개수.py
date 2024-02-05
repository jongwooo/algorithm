import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
cnt = 1
length = 1
for i in range(1, n):
    if a[i - 1] <= a[i]:
        length += 1
    else:
        length = 1
    cnt += length
print(cnt)
