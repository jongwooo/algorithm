word = input().upper()
words = list(set(word))
cnt = []
for w in words:
    cnt.append(word.count(w))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(words[cnt.index(max(cnt))])
