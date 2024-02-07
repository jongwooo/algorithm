import sys

init = int(sys.stdin.readline())
n = init
cnt = 0
while True:
    n = (n % 10) * 10 + ((n // 10) + (n % 10)) % 10
    cnt += 1
    if n == init:
        break
print(cnt)
