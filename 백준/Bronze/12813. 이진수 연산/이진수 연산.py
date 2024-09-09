import sys

a = int(sys.stdin.readline(), 2)
b = int(sys.stdin.readline(), 2)
n = 100_000
mask = 2 ** n - 1
print(bin(a & b)[2:].zfill(n))
print(bin(a | b)[2:].zfill(n))
print(bin(a ^ b)[2:].zfill(n))
print(bin(a ^ mask)[2:].zfill(n))
print(bin(b ^ mask)[2:].zfill(n))
