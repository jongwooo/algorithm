from itertools import permutations


def is_prime_number(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solution(numbers):
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers) + 1):
        per += list(permutations(nums, i))
    new_nums = [int(''.join(p)) for p in per]
    primes = set()
    for n in new_nums:
        if is_prime_number(n):
            primes.add(n)
    return len(primes)
