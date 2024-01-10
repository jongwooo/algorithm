n = int(input())
ropes = sorted([int(input()) for i in range(n)], reverse=True)
max_weight = max([ropes[j] * (j + 1) for j in range(n)])
print(max_weight)
