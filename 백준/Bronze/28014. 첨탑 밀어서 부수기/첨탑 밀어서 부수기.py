import sys

n = int(sys.stdin.readline())
h = list(map(int, sys.stdin.readline().split()))
result = 1
for i in range(n - 1):
    if h[i] <= h[i + 1]:
        result += 1
print(result)
