string = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
for alphabet in alphabets:
    if alphabet in string:
        print(string.index(alphabet), end=' ')
    else:
        print(-1, end=' ')
