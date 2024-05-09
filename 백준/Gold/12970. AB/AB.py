import sys

n, k = map(int, sys.stdin.readline().split())
s = ['B'] * n
cnt = 0
max_cnt = 0
for i in range(n // 2 + 1):
    if max_cnt < i * (n - i):
        max_cnt = i * (n - i)
if max_cnt < k:
    print(-1)
    exit()
while cnt != k:
    idx = n - 1
    cnt -= s.count('A')
    s[idx] = 'A'
    while idx > 0 and s[idx - 1] == 'B' and cnt != k:
        s[idx] = 'B'
        idx -= 1
        s[idx] = 'A'
        cnt += 1
print(''.join(s))
