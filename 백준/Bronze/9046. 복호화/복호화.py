import sys

t = int(sys.stdin.readline())
for _ in range(t):
    alphabets = [0] * 26
    string = sys.stdin.readline().rstrip().replace(' ', '')
    for s in string:
        alphabets[ord(s) - 97] += 1
    if alphabets.count(max(alphabets)) > 1:
        print('?')
    else:
        print(chr(alphabets.index(max(alphabets)) + 97))
