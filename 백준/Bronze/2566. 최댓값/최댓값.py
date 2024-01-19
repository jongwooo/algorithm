import sys

input = sys.stdin.readline

grid = [list(map(int, input().split())) for _ in range(9)]
max_num = 0
y, x = 0, 0
for col in range(9):
    for row in range(9):
        if max_num < grid[col][row]:
            max_num = grid[col][row]
            y, x = col, row
print(max_num)
print(y + 1, x + 1)
