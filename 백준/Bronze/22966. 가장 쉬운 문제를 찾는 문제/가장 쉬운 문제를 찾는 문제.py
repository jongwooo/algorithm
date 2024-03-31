import sys

n = int(sys.stdin.readline())
questions = []
for _ in range(n):
    name, difficulty = sys.stdin.readline().rstrip().split()
    questions.append((name, int(difficulty)))
questions.sort(key=lambda x: x[1])
print(questions[0][0])
