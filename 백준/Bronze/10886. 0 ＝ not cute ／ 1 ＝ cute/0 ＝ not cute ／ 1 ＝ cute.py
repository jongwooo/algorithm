import sys


def input():
    return sys.stdin.readline()


n = int(input())
cute = 0
for _ in range(n):
    v = int(input())
    if v == 1:
        cute += 1
    else:
        cute -= 1
print(f'Junhee is{" " if cute > 0 else " not "}cute!')
