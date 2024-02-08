import sys

string = sys.stdin.readline().rstrip()
vowels = ('a', 'e', 'i', 'o', 'u')
cnt = 0
for s in string:
    if s in vowels:
        cnt += 1
print(cnt)
