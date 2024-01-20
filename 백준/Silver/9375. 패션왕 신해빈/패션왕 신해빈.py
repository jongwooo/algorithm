t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        cloth = input().split()[1]
        if cloth not in clothes:
            clothes[cloth] = 1
        else:
            clothes[cloth] += 1
    result = 1
    for cnt in clothes.values():
        result *= (cnt + 1)
    print(result - 1)
