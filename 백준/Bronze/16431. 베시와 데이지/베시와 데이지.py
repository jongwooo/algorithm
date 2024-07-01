import sys

br, bc = map(int, sys.stdin.readline().split())
dr, dc = map(int, sys.stdin.readline().split())
jr, jc = map(int, sys.stdin.readline().split())
b = max(abs(jr - br), abs(jc - bc))
d = abs(jr - dr) + abs(jc - dc)
if b == d:
    print('tie')
elif b < d:
    print('bessie')
else:
    print('daisy')
