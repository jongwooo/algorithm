t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    s1 = sorted(list(input().split()))
    s2 = sorted(list(input().split()))
    p1, p2 = 0, 0
    cnt = 0
    while p1 < n and p2 < m:
        if s1[p1] == s2[p2]:
            cnt += 1
            p1 += 1
            p2 += 1
        elif s1[p1] < s2[p2]:
            p1 += 1
        else:
            p2 += 1
    print(f'#{test_case} {cnt}')
