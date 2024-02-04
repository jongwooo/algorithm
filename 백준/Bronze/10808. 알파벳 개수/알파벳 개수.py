import sys

alphabet = [0] * 26
string = sys.stdin.readline().rstrip()
for s in string:
    alphabet[ord(s) - ord('a')] += 1
print(*alphabet)
