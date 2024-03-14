import sys

n = int(sys.stdin.readline())
if n <= 28:
    for i in range(1, 8):
        if n <= i * (i + 1) // 2:
            print(i)
            break
else:
    print((n - 29) // 7 + 8)
