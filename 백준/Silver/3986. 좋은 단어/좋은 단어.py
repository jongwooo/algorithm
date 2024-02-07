import sys

n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    stack = []
    for w in word:
        if stack and stack[-1] == w:
            stack.pop()
        else:
            stack.append(w)
    if not stack:
        cnt += 1
print(cnt)
