import sys

n, k = map(int, sys.stdin.readline().split())
factors = []
for i in range(1, n + 1):
    if n % i == 0:
        factors.append(i)
print(0 if k > len(factors) else factors[k - 1])
