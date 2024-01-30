import sys


def input():
    return sys.stdin.readline()


v = int(input())
votes = input()
a, b = 0, 0
for i in range(v):
    if votes[i] == 'A':
        a += 1
    else:
        b += 1
if a > b:
    print('A')
elif a < b:
    print('B')
else:
    print('Tie')
