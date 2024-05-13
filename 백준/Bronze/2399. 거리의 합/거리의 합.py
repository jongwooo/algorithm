import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
total = 0
for i in range(n):
    temp = 0
    for j in range(i, n):
        temp += abs(x[i] - x[j])
    total += temp * 2
print(total)
