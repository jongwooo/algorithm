import sys

n = int(sys.stdin.readline())
result = 0
while n > 0:
    result += (n % 10) ** 5
    n //= 10
print(result)
