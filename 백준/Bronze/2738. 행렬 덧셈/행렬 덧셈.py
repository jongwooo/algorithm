n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(n)]
for col in range(n):
    for row in range(m):
        print(matrix1[col][row] + matrix2[col][row], end=' ')
    print()
