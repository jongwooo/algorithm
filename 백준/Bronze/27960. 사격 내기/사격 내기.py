import sys

a, b = map(int, sys.stdin.readline().split())
score = 512
c = 0
while score > 0:
    cnt = 0
    if score <= a:
        cnt += 1
        a -= score
    if score <= b:
        cnt += 1
        b -= score
    if cnt == 1:
        c += score
    score >>= 1
print(c)
