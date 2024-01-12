while True:
    sides = sorted(list(map(int, input().split())))
    if sum(sides) == 0:
        break
    print("right" if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2 else "wrong")
