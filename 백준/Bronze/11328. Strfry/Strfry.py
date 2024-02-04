import sys

n = int(sys.stdin.readline())
for _ in range(n):
    alphabet = [0] * 26
    str1, str2 = sys.stdin.readline().split()
    for c in str1:
        alphabet[ord(c) - ord('a')] += 1
    for c in str2:
        alphabet[ord(c) - ord('a')] -= 1
    print('Possible' if all(x == 0 for x in alphabet) else 'Impossible')
