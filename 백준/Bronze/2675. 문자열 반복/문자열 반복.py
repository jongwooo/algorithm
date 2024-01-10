n = int(input())
for _ in range(n):
    cnt, word = input().split()
    for w in word:
        print(w * int(cnt), end='')
    print()
