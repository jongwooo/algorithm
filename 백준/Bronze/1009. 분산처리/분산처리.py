t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        if b % 2 == 0:
            print((a ** 2) % 10)
        else:
            print(a)
    elif a == 2 or a == 3 or a == 7 or a == 8:
        if b % 4 == 0:
            print(a ** 4 % 10)
        else:
            print(a ** (b % 4) % 10)
