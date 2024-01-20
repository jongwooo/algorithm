x = []
y = []
for _ in range(3):
    i, j = map(int, input().split())
    if i not in x:
        x.append(i)
    else:
        x.remove(i)
    if j not in y:
        y.append(j)
    else:
        y.remove(j)
print(*x, *y)
