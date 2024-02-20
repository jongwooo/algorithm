import sys

s = sys.stdin.readline().rstrip()
arr = sorted([s[i:] for i in range(len(s))])
for a in arr:
    print(a)
