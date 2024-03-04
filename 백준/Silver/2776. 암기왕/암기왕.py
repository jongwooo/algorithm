import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    note1 = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    note2 = list(map(int, sys.stdin.readline().split()))
    for num in note2:
        print(1 if num in note1 else 0)
