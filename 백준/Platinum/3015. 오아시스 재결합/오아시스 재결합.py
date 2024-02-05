import sys

n = int(sys.stdin.readline())
heights = [int(sys.stdin.readline()) for _ in range(n)]
stack = []
cnt = 0
for height in heights:
    while stack and stack[-1][0] < height:
        cnt += stack.pop()[1]
    if not stack:
        stack.append((height, 1))
    elif stack[-1][0] == height:
        temp = stack.pop()[1]
        cnt += temp
        if stack:
            cnt += 1
        stack.append((height, temp + 1))
    else:
        stack.append((height, 1))
        cnt += 1
print(cnt)
