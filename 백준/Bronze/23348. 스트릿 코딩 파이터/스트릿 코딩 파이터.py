import sys

level = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
grades = []
for i in range(n):
    grade = 0
    for j in range(3):
        a = list(map(int, sys.stdin.readline().split()))
        for k in range(3):
            grade += a[k] * level[k]
    grades.append(grade)
print(max(grades))
