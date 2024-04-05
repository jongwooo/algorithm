import sys


def check_alphabets(arr):
    vowel_cnt, consonant_cnt = 0, 0
    for a in arr:
        if a in vowels:
            vowel_cnt += 1
        else:
            consonant_cnt += 1
    if vowel_cnt >= 1 and consonant_cnt >= 2:
        return True
    return False


def backtracking(arr):
    if len(arr) == L:
        if check_alphabets(arr):
            print(''.join(arr))
            return
    for i in range(len(arr), C):
        if arr[-1] < words[i]:
            arr.append(words[i])
            backtracking(arr)
            arr.pop()


L, C = map(int, sys.stdin.readline().split())
vowels = ('a', 'e', 'i', 'o', 'u')
words = sys.stdin.readline().rstrip().split()
words.sort()
for i in range(C - L + 1):
    backtracking([words[i]])
