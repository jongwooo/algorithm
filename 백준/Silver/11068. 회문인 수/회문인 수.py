import sys


def convert(n, b):
    q, r = divmod(n, b)
    if q == 0:
        return base[r]
    return convert(q, b) + base[r]


def is_palindrome(s):
    return s == s[::-1]


base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz#$"
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    flag = 0
    for b in range(2, 65):
        if is_palindrome(convert(n, b)):
            flag = 1
            break
    print(flag)
