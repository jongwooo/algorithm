import sys

n, k = map(int, sys.stdin.readline().split())
result = []
for i in range(n):
    m = int(sys.stdin.readline())
    fishing = list(map(int, sys.stdin.readline().split()))
    max_distance = 0
    for j in range(0, 2 * m, 2):
        if max_distance < fishing[j] ** 2 + fishing[j + 1] ** 2:
            max_distance = fishing[j] ** 2 + fishing[j + 1] ** 2
    result.append(max_distance)
result.sort()
print(f'{result[k - 1]:.2f}')
