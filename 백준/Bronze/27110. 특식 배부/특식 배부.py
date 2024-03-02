import sys

n = int(sys.stdin.readline())
a, b, c = map(int, sys.stdin.readline().split())
cnt = 0
cnt += a if n > a else n
cnt += b if n > b else n
cnt += c if n > c else n
print(cnt)
