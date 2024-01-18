string = input()
result = ''
temp = ''
tag = False
for s in string:
    if s == '<':
        result += temp[::-1] + s
        temp = ''
        tag = True
    elif s == '>':
        result += s
        tag = False
    elif tag:
        result += s
    else:
        if s == ' ':
            result += temp[::-1] + s
            temp = ''
        else:
            temp += s
result += temp[::-1]
print(result)
