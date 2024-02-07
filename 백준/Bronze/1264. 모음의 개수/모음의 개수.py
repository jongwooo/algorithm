import sys

vowels = ('a', 'e', 'i', 'o', 'u')
while True:
    string = sys.stdin.readline().rstrip()
    if string == '#':
        break
    cnt = 0
    for s in string.lower():
        if s in vowels:
            cnt += 1
    print(cnt)
