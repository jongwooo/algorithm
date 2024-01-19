dic = {
    'A+': '4.5', 'A0': '4.0',
    'B+': '3.5', 'B0': '3.0',
    'C+': '2.5', 'C0': '2.0',
    'D+': '1.5', 'D0': '1.0',
    'F': '0.0'
}
credit = 0
score_sum = 0
for _ in range(20):
    _, c, g = input().split()
    if g == 'P':
        continue
    score_sum += float(c) * float(dic[g])
    credit += float(c)
print(score_sum / credit)
