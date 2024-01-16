import math

n = int(input())
num = math.factorial(n)
cnt = 0
while num % 10 == 0:
    num //= 10
    cnt += 1
print(cnt)
