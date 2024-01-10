n = int(input())
equipments = sorted(list(map(int, input().split())))
loss = []
if n % 2 != 0:
    loss.append(equipments[-1])
    equipments = equipments[:-1]
for i in range(n // 2):
    loss.append(equipments[i] + equipments[-1 - i])
print(max(loss))
