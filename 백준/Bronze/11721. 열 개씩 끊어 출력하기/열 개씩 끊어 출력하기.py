import sys

string = sys.stdin.readline()
for i in range(len(string) // 10 + 1):
    print(string[10 * i:10 * i + 10])
