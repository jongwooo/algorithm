import sys

input = sys.stdin.readline

n, m = map(int, input().split())
trains = [0] * (n + 1)
commands = [list(map(int, input().split())) for _ in range(m)]
for command in commands:
    if command[0] == 1:
        _, i, x = command
        trains[i] |= (1 << (x - 1))
    elif command[0] == 2:
        _, i, x = command
        trains[i] &= ~(1 << (x - 1))
    elif command[0] == 3:
        _, i = command
        trains[i] = trains[i] << 1
        trains[i] &= ((1 << 20) - 1)
    elif command[0] == 4:
        _, i = command
        trains[i] = trains[i] >> 1
result = set(trains[1:])
print(len(result))
