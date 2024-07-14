import sys

n = int(sys.stdin.readline())
alphabets = [chr(i) for i in range(97, 123)]
for _ in range(n):
    s = sys.stdin.readline().rstrip().lower()
    result = ''
    for a in alphabets:
        if s.find(a) == -1:
            result += a
    print('pangram' if not result else f'missing {result}')
