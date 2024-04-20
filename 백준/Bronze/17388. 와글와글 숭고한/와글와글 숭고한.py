import sys

s, k, h = map(int, sys.stdin.readline().split())
if s + k + h >= 100:
    print('OK')
else:
    min_univ = min(s, k, h)
    if min_univ == s:
        print('Soongsil')
    elif min_univ == k:
        print('Korea')
    elif min_univ == h:
        print('Hanyang')
