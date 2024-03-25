import sys

n, m = map(int, sys.stdin.readline().split())
ki = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(1, n + 1):
    for k in ki:
        if i % k == 0:
            result += i
            break
print(result)
