import sys

n = int(sys.stdin.readline())
cnt = 0
i = 1
while i * i <= n:
    i += 1
    cnt += 1
print(cnt)
