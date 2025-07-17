import sys

n = int(sys.stdin.readline())
v = list(map(int, sys.stdin.readline().split()))
cnt = 1
result = 0
for  i in range(n - 1, -1, -1):
    if cnt <= v[i]:
        result += cnt
        cnt += 1
    else:
        result += v[i]
        cnt = v[i] + 1
print(result)
