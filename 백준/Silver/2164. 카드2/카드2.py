import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
cards = deque([(i + 1) for i in range(n)])
while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
print(*cards)
