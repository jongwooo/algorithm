import sys

t = int(sys.stdin.readline())
for _ in range(t):
    data = sys.stdin.readline().split()
    idx = int(data[0])
    string = data[1]
    print(string[:idx - 1] + string[idx:])
