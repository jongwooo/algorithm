import sys

n = int(sys.stdin.readline())
alphabets = [0] * 26
song = sys.stdin.readline().rstrip()
for s in song:
    if s == ' ' or s == ',' or s == '.':
        continue
    alphabets[ord(s) - ord('a')] += 1
print(max(alphabets))
