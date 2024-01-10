n = int(input())
times = sorted(list(map(int, input().split())))
print(sum(times[i] * (n - i) for i in range(n)))
