n = int(input())
extensions = [input().split('.')[1] for _ in range(n)]
counter = {}
for extension in extensions:
    if extension in counter:
        counter[extension] += 1
    else:
        counter[extension] = 1
for extension, count in sorted(counter.items()):
    print(extension, count)
