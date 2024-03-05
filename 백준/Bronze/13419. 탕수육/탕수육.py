import sys

t = int(sys.stdin.readline())
for _ in range(t):
    string = sys.stdin.readline().rstrip()
    a = ''
    b = ''
    if len(string) % 2 != 0:
        string = string * 2
    for i in range(len(string)):
        if i % 2 == 0:
            a += string[i]
        else:
            b += string[i]
    print(a)
    print(b)
