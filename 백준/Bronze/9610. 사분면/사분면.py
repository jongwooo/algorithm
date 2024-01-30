import sys

n = int(sys.stdin.readline())
q = [0] * 5
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if x > 0 and y > 0:
        q[1] += 1
    elif x < 0 < y:
        q[2] += 1
    elif x < 0 and y < 0:
        q[3] += 1
    elif y < 0 < x:
        q[4] += 1
    else:
        q[0] += 1
for i in range(1, 5):
    print(f'Q{i}: {q[i]}')
print(f'AXIS: {q[0]}')
