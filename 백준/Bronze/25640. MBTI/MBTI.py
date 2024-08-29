import sys

jinho = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    friend = sys.stdin.readline().rstrip()
    if jinho == friend:
        cnt += 1
print(cnt)
