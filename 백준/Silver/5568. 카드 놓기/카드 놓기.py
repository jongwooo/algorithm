import sys
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
k = int(input())
cards = [input() for _ in range(n)]
print(len(set(''.join(i) for i in permutations(cards, k))))
