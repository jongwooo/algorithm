n = int(input())
colors = input()
color_dict = {'B': 0, 'R': 0}
current_color = ''
for color in colors:
    if current_color != color:
        color_dict[color] += 1
        current_color = color
print(color_dict['R'] + 1 if color_dict['B'] > color_dict['R'] else color_dict['B'] + 1)
