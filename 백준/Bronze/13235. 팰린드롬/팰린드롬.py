import sys

string = sys.stdin.readline().rstrip()
print('true' if string == string[::-1] else 'false')
