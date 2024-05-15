import sys


def anagrams(a, b):
    return sorted(a) == sorted(b)


t = int(sys.stdin.readline())
for _ in range(t):
    a, b = sys.stdin.readline().rstrip().split()
    print(f'{a} & {b} are {"" if anagrams(a, b) else "NOT "}anagrams.')
