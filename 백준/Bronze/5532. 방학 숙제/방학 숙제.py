import sys

L = int(sys.stdin.readline())
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = A // C
F = B // D
if E > F:
    if A % C == 0:
        print(L - E)
    else:
        print(L - E - 1)
else:
    if B % D == 0:
        print(L - F)
    else:
        print(L - F - 1)
