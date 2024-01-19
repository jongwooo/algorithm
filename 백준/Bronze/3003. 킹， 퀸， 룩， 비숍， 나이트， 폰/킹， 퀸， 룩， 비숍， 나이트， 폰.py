black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
diff = [b - w for b, w in zip(black, white)]
print(*diff)
