tc = int(input())
for test_case in range(1, tc + 1):
    n, m = map(int, input().split())
    s = list(input().split())
    t = list(input().split())
    q = int(input())
    years = [int(input()) for _ in range(q)]
    names = []
    for y in years:
        s_idx = (y - 1) % len(s)
        t_idx = (y - 1) % len(t)
        names.append(s[s_idx] + t[t_idx])
    print(f'#{test_case} {" ".join(names)}')
