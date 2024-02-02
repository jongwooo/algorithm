import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b, c = sorted(map(int, sys.stdin.readline().split()))
    print(f'Scenario #{i + 1}:\n{"yes" if c ** 2 == a ** 2 + b ** 2 else "no"}\n')
