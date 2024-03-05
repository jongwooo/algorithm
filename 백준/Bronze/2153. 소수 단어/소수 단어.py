import sys


def is_prime_number(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


word = sys.stdin.readline().rstrip()
alphabets = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = 0
for w in word:
    num += alphabets.index(w)
print(f'It is {"" if is_prime_number(num) else "not "}a prime word.')
