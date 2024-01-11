n, m = map(int, input().split())
bulbs = list(map(int, input().split()))
for _ in range(m):
    command, option1, option2 = map(int, input().split())
    if command == 1:
        bulbs[option1 - 1] = option2
    elif command == 2:
        bulbs[option1 - 1:option2] = [1 - bulb for bulb in bulbs[option1 - 1:option2]]
    elif command == 3:
        bulbs[option1 - 1:option2] = [0] * (option2 - option1 + 1)
    elif command == 4:
        bulbs[option1 - 1:option2] = [1] * (option2 - option1 + 1)
print(*bulbs)
