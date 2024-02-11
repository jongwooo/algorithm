import sys

while True:
    string = sys.stdin.readline().rstrip()
    if string == 'END':
        break
    print(string[::-1])
