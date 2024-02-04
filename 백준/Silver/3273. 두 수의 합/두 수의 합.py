import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())
left, right = 0, n-1
cnt = 0
while left < right:
    temp = a[left] + a[right]
    if temp == x:
        cnt += 1
        left += 1
    elif temp < x:
        left += 1
    else:
        right -= 1
print(cnt)
