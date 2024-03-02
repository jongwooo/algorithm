import sys

n = int(sys.stdin.readline())
for _ in range(n):
    nicknames = sys.stdin.readline().rstrip().split()
    nicknames[0] = 'god'
    print(''.join(nicknames))
