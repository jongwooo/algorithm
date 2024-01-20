paper = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            if paper[i][j] == 0:
                paper[i][j] = 1
area = 0
for p in paper:
    area += sum(p)
print(area)
