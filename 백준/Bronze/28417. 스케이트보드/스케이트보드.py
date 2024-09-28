import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    skateboard = list(map(int, sys.stdin.readline().split()))
    run = skateboard[:2]
    trick = skateboard[2:]
    run.sort(reverse=True)
    trick.sort(reverse=True)
    result = max(result, run[0] + sum(trick[:2]))
print(result)
