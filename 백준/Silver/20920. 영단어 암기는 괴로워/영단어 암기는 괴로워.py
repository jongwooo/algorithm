import sys

n, m = map(int, sys.stdin.readline().split())
word_book = dict()
for _ in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue
    elif word not in word_book:
        word_book[word] = [1, len(word), word]
    else:
        word_book[word][0] += 1
result = sorted(word_book.values(), key=lambda x: (-x[0], -x[1], x[2]))
for _, _, w in result:
    print(w)
