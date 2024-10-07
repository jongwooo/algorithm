import sys

retake_code = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
subjects = [sys.stdin.readline().rstrip() for _ in range(n)]
result = 0
for subject in subjects:
    if retake_code[:5] == subject[:5]:
        result += 1
print(result)
