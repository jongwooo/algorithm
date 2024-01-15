string = input()
result = ''
for s in string:
    if s.isupper():
        result += s.lower()
    else:
        result += s.upper()
print(result)
