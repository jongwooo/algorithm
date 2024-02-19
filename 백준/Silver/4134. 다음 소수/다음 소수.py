import sys


def is_prime_number(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    while True:
        if is_prime_number(n):
            print(n)
            break
        n += 1