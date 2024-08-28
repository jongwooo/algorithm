import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    x = int(sys.stdin.readline().rstrip()[2:])
    if x <= 90:
        cnt += 1
print(cnt)
