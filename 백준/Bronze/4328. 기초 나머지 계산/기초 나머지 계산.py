import sys


def base_n(num, n):
    result = ''
    while num >= n:
        result += str(num % n)
        num //= n
    result += str(num)
    return result[::-1]


while True:
    tc = sys.stdin.readline().rstrip()
    if tc == '0':
        break
    b, p, m = tc.split()
    b = int(b)
    p = int(p, b)
    m = int(m, b)
    print(base_n(p % m, b))
