keyboard = {
    'q': ('l', 0, 0),
    'w': ('l', 0, 1),
    'e': ('l', 0, 2),
    'r': ('l', 0, 3),
    't': ('l', 0, 4),
    'a': ('l', 1, 0),
    's': ('l', 1, 1),
    'd': ('l', 1, 2),
    'f': ('l', 1, 3),
    'g': ('l', 1, 4),
    'z': ('l', 2, 0),
    'x': ('l', 2, 1),
    'c': ('l', 2, 2),
    'v': ('l', 2, 3),
    'y': ('r', 0, 5),
    'u': ('r', 0, 6),
    'i': ('r', 0, 7),
    'o': ('r', 0, 8),
    'p': ('r', 0, 9),
    'h': ('r', 1, 5),
    'j': ('r', 1, 6),
    'k': ('r', 1, 7),
    'l': ('r', 1, 8),
    'b': ('r', 2, 4),
    'n': ('r', 2, 5),
    'm': ('r', 2, 6),
}
sl, sr = input().split()
word = input()
cnt = 0
for key in word:
    if keyboard[key][0] == 'l':
        cnt += abs(keyboard[sl][1] - keyboard[key][1]) + abs(keyboard[sl][2] - keyboard[key][2]) + 1
        sl = key
    else:
        cnt += abs(keyboard[sr][1] - keyboard[key][1]) + abs(keyboard[sr][2] - keyboard[key][2]) + 1
        sr = key
print(cnt)
