n = int(input())
cnt = n
for _ in range(n):
    string = input()
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            continue
        else:
            if string[i] in string[i + 2:]:
                cnt -= 1
                break
print(cnt)
