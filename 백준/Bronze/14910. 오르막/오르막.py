import sys

n = list(map(int, sys.stdin.readline().split()))
print('Good' if n == sorted(n) else 'Bad')
