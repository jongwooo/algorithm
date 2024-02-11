import sys

n = int(sys.stdin.readline())
for _ in range(n):
    string = sys.stdin.readline().rstrip()
    print(string[0].upper() + string[1:])
