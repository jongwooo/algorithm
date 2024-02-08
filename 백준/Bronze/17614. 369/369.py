import sys

n = int(sys.stdin.readline())
cnt = 0
while n > 0:
    str_n = str(n)
    cnt += str_n.count('3')
    cnt += str_n.count('6')
    cnt += str_n.count('9')
    n -= 1
print(cnt)
