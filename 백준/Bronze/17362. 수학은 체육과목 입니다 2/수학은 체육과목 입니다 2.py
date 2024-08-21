import sys

n = int(sys.stdin.readline()) % 8
result = 1
if n == 0 or n == 2:
    result = 2
elif n == 3 or n == 7:
    result = 3
elif n == 4 or n == 6:
    result = 4
elif n == 5:
    result = 5
print(result)
