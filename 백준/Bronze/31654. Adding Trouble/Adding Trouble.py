import sys

a, b, c = map(int, sys.stdin.readline().split())
print('correct!' if a + b == c else 'wrong!')
