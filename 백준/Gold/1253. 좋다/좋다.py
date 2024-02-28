import sys

N = int(sys.stdin.readline())
A = sorted(list(map(int, sys.stdin.readline().split())))
cnt = 0

for i in range(N):
    attempt = A[i]
    start, end = 0, N - 1
    while start < end:
        if A[start] + A[end] == attempt:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif A[start] + A[end] < attempt:
            start += 1
        elif A[start] + A[end] > attempt:
            end -= 1
print(cnt)
