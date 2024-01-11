n = int(input())
times = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
cnt = 0
prev_end = 0
for start, end in times:
    if prev_end <= start:
        cnt += 1
        prev_end = end
print(cnt)
