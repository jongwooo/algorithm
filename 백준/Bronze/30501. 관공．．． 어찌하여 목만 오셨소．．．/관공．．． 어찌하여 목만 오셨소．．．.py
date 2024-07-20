import sys

n = int(sys.stdin.readline())
criminal = ''
for _ in range(n):
    suspect = sys.stdin.readline().rstrip()
    if 'S' in suspect:
        criminal = suspect
print(criminal)
