import sys

n = int(sys.stdin.readline())
for _ in range(n):
    password = sys.stdin.readline().rstrip()
    print('yes' if 6 <= len(password) <= 9 else 'no')
