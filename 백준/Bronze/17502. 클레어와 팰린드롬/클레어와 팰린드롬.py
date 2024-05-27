import sys

n = int(sys.stdin.readline())
palindrome = list(sys.stdin.readline().rstrip())
for i in range(n):
    if palindrome[i].isalpha():
        palindrome[-i - 1] = palindrome[i]
for i in range(n):
    if palindrome[i] == '?':
        palindrome[i] = 'a'
print(''.join(palindrome))
