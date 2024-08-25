import sys

t = int(sys.stdin.readline())
a1 = (1, 3, 5, 7, 8, 10, 12)
a2 = (4, 6, 9, 11)
for _ in range(t):
    A = 'No'
    B = 'No'
    a, b, = map(int, sys.stdin.readline().split())
    if 0 < a <= 12:
        if a in a1 and 0 < b <= 31:
            A = 'Yes'
        elif a in a2 and 0 < b <= 30:
            A = 'Yes'
        elif a == 2 and 0 < b <= 29:
            A = 'Yes'
    if 0 <= a <= 23:
        if b <= 59:
            B = 'Yes'
    print(B, A)
