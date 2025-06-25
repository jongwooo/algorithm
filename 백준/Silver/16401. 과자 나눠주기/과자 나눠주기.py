import sys

m, n = map(int, sys.stdin.readline().split())
l = sorted(list(map(int, sys.stdin.readline().split())))
start = 1
end =l[-1]
result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in l:
        if i < mid:
            continue
        cnt += i // mid
    if m <= cnt:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
