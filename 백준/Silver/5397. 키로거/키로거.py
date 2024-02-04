import sys

t = int(sys.stdin.readline())
for _ in range(t):
    keyboard = sys.stdin.readline().rstrip()
    left, right = [], []
    for k in keyboard:
        if k == '<':
            if left:
                right.append(left.pop())
        elif k == '>':
            if right:
                left.append(right.pop())
        elif k == '-':
            if left:
                left.pop()
        else:
            left.append(k)
    left.extend(reversed(right))
    print(''.join(left))
