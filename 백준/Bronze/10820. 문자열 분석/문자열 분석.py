import sys

while True:
    data = sys.stdin.readline().rstrip('\n')
    if not data:
        break
    l, u, d, s = 0, 0, 0, 0
    for v in data:
        if v.islower():
            l += 1
        elif v.isupper():
            u += 1
        elif v.isdigit():
            d += 1
        elif v.isspace():
            s += 1
    print(l, u, d, s)
