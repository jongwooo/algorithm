n, m = map(int, input().split())
unheard = set()
for _ in range(n):
    unheard.add(input())
unseen = set()
for _ in range(m):
    unseen.add(input())
both = sorted(list(unheard & unseen))
print(len(both))
for b in both:
    print(b)
