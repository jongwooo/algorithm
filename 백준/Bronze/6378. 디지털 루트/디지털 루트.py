import sys


def digital_root(n):
    if len(n) == 1:
        return n
    return digital_root(str(sum(map(int, list(n)))))


while True:
    n = sys.stdin.readline().rstrip()
    if n == '0':
        break
    print(digital_root(n))
