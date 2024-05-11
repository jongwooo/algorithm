import sys

H, I, A, R, C = map(int, sys.stdin.readline().split())
print(H * I - A * R * C)
