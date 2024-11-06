import sys

arr = [float(sys.stdin.readline()) for i in range(10)]
ans = 1
for i in arr:
    ans *= i
ans /= min(arr)
print(round(ans / 0.00036288, 7))
