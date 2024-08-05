import sys

l, k, p = False, False, False
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
s3 = sys.stdin.readline().rstrip()
for s in s1[0], s2[0], s3[0]:
    if s == 'l':
        l = True
    elif s == 'k':
        k = True
    elif s == 'p':
        p = True
print('GLOBAL' if l and k and p else 'PONIX')
