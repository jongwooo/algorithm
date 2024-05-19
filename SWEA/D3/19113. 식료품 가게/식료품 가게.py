tc = int(input())
for t in range(1, tc + 1):
    n = int(input())
    p = list(map(int, input().split()))
    result = []
    while p:
        for i in range(len(p)):
            if p[i] % 4 == 0 and int(p[i] * 0.75) in p:
                a = p.pop(i)
                result.append(p.pop(p.index(int(a * 0.75))))
                break
    print(f'#{t} {" ".join(list(map(str, result)))}')
