import sys

a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
a_num = list(map(int, sys.stdin.readline().split()))
a_num.reverse()
decimal_num = 0
for i in range(m):
    decimal_num += a_num[i] * (a ** i)
b_num = []
while decimal_num > 0:
    b_num.append(decimal_num % b)
    decimal_num //= b
print(*b_num[::-1])
