import sys

s = sys.stdin.readline().rstrip()
print(s[1:-1] if s[0] == '\"' and s[-1] == '\"' and len(s) > 2 else 'CE')
