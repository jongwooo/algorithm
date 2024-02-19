import sys

m, s = map(int, sys.stdin.readline().split(':'))
cnt = 1
cnt += (m // 10 + m % 10)
cnt += (s // 10) if s < 30 else ((s - 30) // 10)
print(cnt)
