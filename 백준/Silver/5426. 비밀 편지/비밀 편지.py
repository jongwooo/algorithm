import sys


def rotate(msg):
    size = int(len(msg) ** 0.5)
    arr = [[''] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            arr[size - j - 1][i] = msg[size * i + j]
    return arr


t = int(sys.stdin.readline())
for _ in range(t):
    msg = sys.stdin.readline().rstrip()
    rotated = rotate(msg)
    for a in rotated:
        print(''.join(a), end='')
    print()
