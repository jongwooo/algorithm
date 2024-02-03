import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    student, apple = map(int, sys.stdin.readline().split())
    result += apple % student
print(result)
