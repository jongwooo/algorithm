import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
alphabet = [0] * 26
for c in str1:
    alphabet[ord(c) - ord('a')] += 1
for c in str2:
    alphabet[ord(c) - ord('a')] -= 1
print(sum(map(abs, alphabet)))
