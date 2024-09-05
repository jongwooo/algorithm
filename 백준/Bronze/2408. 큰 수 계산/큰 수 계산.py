import sys

n = int(sys.stdin.readline())
arithmetic = ''
for _ in range(2 * n + 1):
    arithmetic += sys.stdin.readline().rstrip()
arithmetic = arithmetic.replace('/', '//')
print(eval(arithmetic))
