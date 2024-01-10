n = int(input())
for _ in range(n):
    results = input().split('X')
    point = 0
    for result in results:
        point += len(result) * (len(result) + 1) // 2
    print(point)
