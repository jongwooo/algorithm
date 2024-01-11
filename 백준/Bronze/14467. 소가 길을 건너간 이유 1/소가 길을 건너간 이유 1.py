n = int(input())
data = sorted([tuple(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
cnt = 0
current_cow, current_loc = 0, 0
for cow, location in data:
    if current_cow != cow:
        current_cow = cow
        current_loc = location
        continue
    if current_loc != location:
        current_loc = location
        cnt += 1
print(cnt)
