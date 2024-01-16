t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    residents = [i for i in range(1, n + 1)]
    for _ in range(k):
        for number in range(1, n):
            residents[number] += residents[number - 1]
    print(residents[-1])
