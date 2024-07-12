import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
characters = []
for c in range(0, n * 6, 6):
    characters.append(s[c: c + 6])
promise = ('000000', '001111', '010011', '011100', '100110', '101001', '110101', '111010')
correct = ''
incorrect = 0
for c in characters:
    incorrect = 0
    for p in promise:
        cnt = 0
        for k in range(6):
            if c[k] == p[k]:
                cnt += 1
        if cnt >= 5:
            correct += chr(promise.index(p) + 65)
            break
        else:
            incorrect += 1
    if incorrect == len(promise):
        print(characters.index(c) + 1)
        quit()
print(correct)
