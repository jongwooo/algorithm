import sys

while True:
    a, *info = map(int, sys.stdin.readline().split())
    if a == 0:
        break
    leaf = 1
    for i in range(0, 2 * a, 2):
        leaf = leaf * info[i] - info[i + 1]
    print(leaf)
