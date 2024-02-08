import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]
max_h = 0
cnt = 0
for h in heights[::-1]:
    if max_h < h:
        max_h = h
        cnt += 1
print(cnt)
