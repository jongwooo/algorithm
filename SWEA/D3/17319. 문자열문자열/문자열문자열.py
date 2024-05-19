tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    s = input()
    if n % 2 == 0 and s[:n // 2] == s[n // 2:]:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')
