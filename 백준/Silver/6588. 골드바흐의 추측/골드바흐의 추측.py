import sys

prime = [True for _ in range(1_000_001)]
prime[1] = False
for i in range(2, int(len(prime) ** 0.5) + 1):
    if not prime[i]:
        continue
    for j in range(i + i, len(prime), i):
        prime[j] = False
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    for i in range(3, n // 2 + 1, 2):
        if prime[i] and prime[n - i]:
            print(f'{n} = {i} + {n - i}')
            break
    else:
        print('Goldbach\'s conjecture is wrong.')
