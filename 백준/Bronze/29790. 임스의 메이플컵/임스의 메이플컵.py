import sys

n, u, l = map(int, sys.stdin.readline().split())
if n < 1_000:
    print('Bad')
elif u >= 8_000 or l >= 260:
    print('Very Good')
else:
    print('Good')
