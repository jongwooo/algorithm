string = input()
alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for alphabet in alphabets:
    string = string.replace(alphabet, '*')
print(len(string))
