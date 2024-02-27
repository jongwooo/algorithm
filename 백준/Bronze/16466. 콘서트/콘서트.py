import sys

n = int(sys.stdin.readline())
tickets = sorted(list(map(int, sys.stdin.readline().split())))
yanghan = 1
for ticket in tickets:
    if ticket != yanghan:
        break
    yanghan += 1
print(yanghan)
