def is_palindrome(s):
    return s == s[::-1]


tc = int(input())
for t in range(1, tc + 1):
    n, m = map(int, input().split())
    words = [input() for _ in range(n)]
    palindrome = False
    cnt = 0
    candidates = []
    for word in words:
        if is_palindrome(word):
            palindrome = True
        else:
            candidates.append(word)
    while candidates:
        candidate = candidates.pop()
        if candidate[::-1] in candidates:
            cnt += 2
    result = cnt * m
    if palindrome:
        result += m
    print(f'#{t} {result}')
