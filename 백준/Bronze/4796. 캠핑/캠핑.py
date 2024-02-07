import sys

case = 1
while True:
    l, p, v = map(int, sys.stdin.readline().split())
    if l == p == v == 0:
        break
    a = v // p
    b = v % p
    if l < b:
        b = l
    print(f'Case {case}: {l * a + b}')
    case += 1
