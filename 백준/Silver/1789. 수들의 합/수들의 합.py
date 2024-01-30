import sys

s = int(sys.stdin.readline())
total = 0
cnt = 0
while True:
    cnt += 1
    total += cnt
    if s < total:
        break
print(cnt - 1)
