import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
perfect_square = []
for i in range(m, n + 1):
    num = i ** 0.5
    if int(num) == num:
        perfect_square.append(i)
if perfect_square:
    print(sum(perfect_square))
    print(perfect_square[0])
else:
    print(-1)
