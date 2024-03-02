import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
c = sys.stdin.readline().rstrip()
print('YES' if c in a and c in b else 'NO')
