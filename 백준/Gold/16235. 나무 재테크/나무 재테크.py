import sys
from collections import deque


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def one_year():
    spring()
    summer()
    fall()
    winter()


def spring():
    global tree_cnt
    for r, line in enumerate(trees):
        for c, ages in enumerate(line):
            trees[r][c].sort()
            for i, age in enumerate(ages):
                if age <= nutrients[r][c]:
                    nutrients[r][c] -= age
                    trees[r][c][i] += 1
                    continue
                for j in range(i, len(trees[r][c])):
                    dead_trees.append((r, c, trees[r][c].pop()))
                    tree_cnt -= 1
                break


def summer():
    while dead_trees:
        r, c, age = dead_trees.popleft()
        nutrients[r][c] += age // 2


def fall():
    global tree_cnt
    for r, line in enumerate(trees):
        for c, ages in enumerate(line):
            for age in ages:
                if age % 5 == 0 and age != 0:
                    for dr, dc in dirs:
                        nr = r + dr
                        nc = c + dc
                        if in_range(nr, nc):
                            trees[nr][nc].append(NEW_TREE_AGE)
                            tree_cnt += 1


def winter():
    for r in range(n):
        for c in range(n):
            nutrients[r][c] += a[r][c]


INITIAL_NUTRIENT = 5
NEW_TREE_AGE = 1
dirs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
n, m, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
nutrients = [[INITIAL_NUTRIENT] * n for _ in range(n)]
trees = [[[] for _ in range(n)] for i in range(n)]
dead_trees = deque([])
tree_cnt = 0
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    trees[x - 1][y - 1].append(z)
    tree_cnt += 1
for _ in range(k):
    one_year()
print(tree_cnt)
