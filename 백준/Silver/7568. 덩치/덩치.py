import sys

n = int(sys.stdin.readline())
peoples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            continue
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            cnt += 1
    result.append(cnt)
print(*result)
