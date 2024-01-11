applied = sorted([int(input()) for _ in range(28)])
not_applied = [i for i in range(1, 31) if i not in applied]
print(f'{not_applied[0]}\n{not_applied[1]}')
