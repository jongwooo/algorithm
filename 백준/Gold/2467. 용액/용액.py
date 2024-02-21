import sys

n = int(sys.stdin.readline())
solutions = sorted(list(map(int, sys.stdin.readline().split())))
left, right = 0, n - 1
ans_left, ans_right = left, right
nearest_mixed = abs(solutions[left] + solutions[right])
while left < right:
    mixed = solutions[left] + solutions[right]
    if abs(mixed) < nearest_mixed:
        nearest_mixed = abs(mixed)
        ans_left, ans_right = left, right
    if nearest_mixed == 0:
        break
    if mixed < 0:
        left += 1
    elif mixed > 0:
        right -= 1
print(solutions[ans_left], solutions[ans_right])
