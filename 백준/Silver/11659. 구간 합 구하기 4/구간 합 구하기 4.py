import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + a[i]
for _ in range(m):
    i, j = map(int, input().split())
    print(s[j] - s[i - 1])
