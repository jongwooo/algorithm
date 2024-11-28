import sys

t = int(sys.stdin.readline())
for _ in range(t):
    prob, answer = map(str, sys.stdin.readline().split('='))
    print('correct' if eval(prob) == int(answer) else 'wrong answer')
