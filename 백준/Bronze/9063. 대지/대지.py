n = int(input())
if n == 1:
    print(0)
else:
    dot_x = []
    dot_y = []
    for _ in range(n):
        x, y = map(int, input().split())
        dot_x.append(x)
        dot_y.append(y)
    dot_x.sort()
    dot_y.sort()
    print((dot_x[-1] - dot_x[0]) * (dot_y[-1] - dot_y[0]))
