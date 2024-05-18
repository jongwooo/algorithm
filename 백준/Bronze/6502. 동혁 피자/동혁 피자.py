import sys

pizza_idx = 1
while True:
    data = sys.stdin.readline().rstrip()
    if data == '0':
        break
    r, w, l = map(int, data.split())
    d = (w / 2) ** 2 + (l / 2) ** 2
    print(f'Pizza {pizza_idx} {"fits" if r ** 2 >= d else "does not fit"} on the table.')
    pizza_idx += 1
