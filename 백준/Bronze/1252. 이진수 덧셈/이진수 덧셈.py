import sys

str_a, str_b = sys.stdin.readline().rstrip().split()
a = int(str_a, 2)
b = int(str_b, 2)
print(bin(a + b)[2:])
