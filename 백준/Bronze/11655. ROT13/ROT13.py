import sys

s = sys.stdin.readline().rstrip()
result = ''
for x in s:
    if 'a' <= x <= 'z':
        x = ord(x) + 13
        if x > 122:
            x -= 26
        result += chr(x)
    elif 'A' <= x <= 'Z':
        x = ord(x) + 13
        if x > 90:
            x -= 26
        result += chr(x)
    else:
        result += x
print(result)
