import sys


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


while True:
    num = sys.stdin.readline().strip()
    if int(num) == 0:
        break
    n = len(num)
    result = 0
    for i in range(n):
        result += int(num[i]) * factorial(n - i)
    print(result)
