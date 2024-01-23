import sys
import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
prime_numbers = []
for i in range(m, n + 1):
    if is_prime_number(i):
        prime_numbers.append(i)
if len(prime_numbers) == 0:
    print(-1)
else:
    print(sum(prime_numbers))
    print(min(prime_numbers))
