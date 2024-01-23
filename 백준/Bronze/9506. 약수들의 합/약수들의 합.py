import sys

input = sys.stdin.readline


while True:
    n = int(input())
    if n == -1:
        break
    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)
    if n == sum(factors):
        print(f'{n} =', end=' ')
        print(' + '.join(map(str, factors)))
    else:
        print(f'{n} is NOT perfect.')
