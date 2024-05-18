def is_palindrome(string):
    return string == string[::-1]


t = int(input())
for tc in range(1, t + 1):
    s = input()
    n = len(s)
    print(f'#{tc} {"YES" if is_palindrome(s) and is_palindrome(s[:n // 2]) and is_palindrome(s[::-1][:n // 2]) else "NO"}')
