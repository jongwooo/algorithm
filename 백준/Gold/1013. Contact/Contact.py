import re
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    s = sys.stdin.readline().rstrip()
    p = re.compile('(100+1+|01)+')
    print('YES' if p.fullmatch(s) else 'NO')
