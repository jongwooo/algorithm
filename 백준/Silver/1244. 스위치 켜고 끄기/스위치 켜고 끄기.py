n = int(input())
bulbs = [-1] + list(map(int, input().split()))
s = int(input())


def change_bulb(idx):
    bulbs[idx] = 1 - bulbs[idx]


for _ in range(s):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, n + 1, num):
            change_bulb(i)
    else:
        change_bulb(num)
        for i in range(n // 2):
            if num - i < 1 or num + i > n:
                break
            if bulbs[num - i] == bulbs[num + i]:
                change_bulb(num - i)
                change_bulb(num + i)
            else:
                break

for i in range(1, n + 1):
    print(bulbs[i], end=' ')
    if i % 20 == 0:
        print()
