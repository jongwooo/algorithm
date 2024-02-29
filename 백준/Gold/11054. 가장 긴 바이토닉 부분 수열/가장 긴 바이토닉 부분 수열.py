import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
reverse_a = a[::-1]
incr = [1] * n
desc = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            incr[i] = max(incr[i], incr[j] + 1)
        if reverse_a[i] > reverse_a[j]:
            desc[i] = max(desc[i], desc[j] + 1)
result = [0] * n
for i in range(n):
    result[i] = incr[i] + desc[n - i - 1] - 1
print(max(result))
