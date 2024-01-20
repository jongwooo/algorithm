import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
r = [0] * m
prefix_sum = 0
for i in range(n):
    prefix_sum += a[i]
    r[prefix_sum % m] += 1
ans = r[0]
for i in range(m):
    ans += r[i] * (r[i] - 1) // 2
print(ans)
