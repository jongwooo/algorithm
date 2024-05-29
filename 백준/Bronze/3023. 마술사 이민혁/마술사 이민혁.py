import copy
import sys

r, c = map(int, sys.stdin.readline().split())
cards = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
a, b = map(int, sys.stdin.readline().split())
for i in range(r):
    row = []
    for j in range(c - 1, -1, -1):
        row.append(cards[i][j])
    cards[i].extend(row)
for i in range(r - 1, -1, -1):
    row = copy.deepcopy(cards[i])
    cards.append(row)
if cards[a - 1][b - 1] == '#':
    cards[a - 1][b - 1] = '.'
else:
    cards[a - 1][b - 1] = '#'
for card in cards:
    print(''.join(card))
