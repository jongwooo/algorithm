import sys

RYAN = 1
INF = int(1e9)
n, k = map(int, sys.stdin.readline().split())
dolls = list(map(int, sys.stdin.readline().split()))
min_size = INF
cnt = 0
start = 0
end = 0
if dolls[end] == RYAN:
    cnt += 1
while end < n:
    if cnt == k:
        min_size = min(min_size, end - start + 1)
        if dolls[start] == RYAN:
            cnt -= 1
        start += 1
    else:
        end += 1
        if end < n and dolls[end] == RYAN:
            cnt += 1
print(min_size if min_size != INF else -1)
