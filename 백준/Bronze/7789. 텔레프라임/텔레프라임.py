import sys


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


original, add = sys.stdin.readline().rstrip().split()
original_number = int(original)
add_number = int(add + original)
print('Yes' if is_prime(original_number) and is_prime(add_number) else 'No')
