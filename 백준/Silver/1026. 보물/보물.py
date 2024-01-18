n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
result = 0
for ai, bi in zip(a, b):
    result += ai * bi
print(result)
