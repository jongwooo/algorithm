import sys


def count_pairs_of_integers(n, m):
    cnt = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if (a ** 2 + b ** 2 + m) % (a * b) == 0:
                cnt += 1
    return cnt


t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(count_pairs_of_integers(n, m))
