import sys

input = sys.stdin.readline

m = int(input())
s = 0
for _ in range(m):
    command = input().split()
    if command[0] == 'all':
        s = (1 << 20) - 1
    elif command[0] == 'empty':
        s = 0
    else:
        cmd, number = command[0], command[1]
        number = int(number) - 1
        if cmd == 'add':
            s = s | (1 << number)
        elif cmd == 'remove':
            s = s & ~(1 << number)
        elif cmd == 'check':
            if s & (1 << number) == 0:
                print(0)
            else:
                print(1)
        elif cmd == 'toggle':
            s = s ^ (1 << number)
