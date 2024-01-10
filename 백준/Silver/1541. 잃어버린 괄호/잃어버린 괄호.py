expression = input()
bracket_minus = expression.split('-')
answer = 0
first = sum(map(int, bracket_minus[0].split('+')))
if expression[0] == '-':
    answer -= first
else:
    answer += first
for exp in bracket_minus[1:]:
    answer -= sum(map(int, exp.split('+')))
print(answer)
