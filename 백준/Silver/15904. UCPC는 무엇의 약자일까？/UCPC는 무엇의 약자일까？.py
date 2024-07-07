import sys

string = sys.stdin.readline().rstrip()
ucpc = 'UCPC'
idx = 0
for s in string:
    if s == ucpc[idx]:
        idx += 1
    if idx == len(ucpc):
        break
print(f'I {"love" if idx > 3 else "hate"} UCPC')
