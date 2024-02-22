import sys


def cantor(a, n):
    global line
    if n == 1:
        return
    for i in range(a + n // 3, a + (n // 3) * 2):
        line[i] = ' '
    cantor(a, n // 3)
    cantor(a + (n // 3) * 2, n // 3)


while True:
    try:
        n = int(sys.stdin.readline())
        line = ['-'] * (3 ** n)
        cantor(0, 3 ** n)
        print(''.join(line))
    except:
        break
