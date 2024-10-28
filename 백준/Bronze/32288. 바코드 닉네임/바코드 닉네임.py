import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
for i in s:
    print(i.upper() if i.islower() else i.lower(), end='')
