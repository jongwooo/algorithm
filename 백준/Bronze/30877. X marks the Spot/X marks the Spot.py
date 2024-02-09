import sys

n = int(sys.stdin.readline())
for _ in range(n):
    s, t = sys.stdin.readline().split()
    for i in range(len(s)):
        if s[i] == 'x' or s[i] == 'X':
            print(str(t[i]).upper(), end='')
