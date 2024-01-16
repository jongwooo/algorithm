n = int(input())
words = []
for _ in range(n):
    word = input()
    if word not in words:
        words.append(word)
words.sort()
words.sort(key=len)
for i in range(len(words)):
    print(words[i])
