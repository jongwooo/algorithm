import sys

n = int(sys.stdin.readline())
ans = 0
for i in range(n + 1):
    for j in range(i + 1):
        ans += i + j
print(ans)
