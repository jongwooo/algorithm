import sys

n = int(sys.stdin.readline())
number = int(sys.stdin.readline())
while number:
    if number % n == 0:
        print(f"{number} is a multiple of {n}.")
    else:
        print(f"{number} is NOT a multiple of {n}.")
    number = int(sys.stdin.readline())
