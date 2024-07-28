import sys

n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
for i in range(n - 1, 0, -1):
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            k -= 1
            if k == 0:
                print(f'{a[j]} {a[j + 1]}')
                exit()
print(-1)
