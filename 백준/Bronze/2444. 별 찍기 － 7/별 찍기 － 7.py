n = int(input())
for i in list(range(1, n)) + list(range(n, 0, -1)):
    print(' ' * (n - i) + '*' * (2 * i - 1))
