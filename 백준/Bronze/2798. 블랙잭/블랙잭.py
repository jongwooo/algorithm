n, m = map(int, input().split())
cards = list(map(int, input().split()))
num = 0
for i in range(n - 2):
    for j in range(1, n - 1):
        if i == j:
            continue
        for k in range(2, n):
            if k == i or k == j:
                continue
            temp = cards[i] + cards[j] + cards[k]
            if m >= temp:
                num = max(num, temp)
print(num)
