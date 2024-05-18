import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    words = [sys.stdin.readline().rstrip() for _ in range(n)]
    words.sort(key=str.lower)
    print(words[0])
