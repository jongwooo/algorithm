dials = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
string = input()
time = 0
for dial in dials:
    for i in dial:
        for s in string:
            if i == s:
                time += dials.index(dial) + 3
print(time)
