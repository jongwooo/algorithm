t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    s1 = set(input().split())
    s2 = set(input().split())
    print(f'#{test_case} {len(s1 & s2)}')
