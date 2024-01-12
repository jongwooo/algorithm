board = [list(map(int, input().split())) for _ in range(5)]
speaks = [list(map(int, input().split())) for _ in range(5)]


def check_row():
    row_cnt = 0
    for i in range(5):
        if sum(board[i]) == 0:
            row_cnt += 1
    return row_cnt


def check_col():
    col_cnt = 0
    for i in range(5):
        temp = 0
        for j in range(5):
            if board[j][i] == 0:
                temp += 1
        if temp == 5:
            col_cnt += 1
    return col_cnt


def check_dia():
    dia_cnt = 0
    temp = 0
    for i in range(5):
        if board[i][5 - i - 1] == 0:
            temp += 1
    if temp == 5:
        dia_cnt += 1
    temp = 0
    for i in range(5):
        if board[i][i] == 0:
            temp += 1
    if temp == 5:
        dia_cnt += 1
    return dia_cnt


cnt = 0
speak_idx = 0
for col in range(5):
    for row in range(5):
        speak = speaks[col][row]
        speak_idx += 1
        for y in range(5):
            for x in range(5):
                if board[y][x] == speak:
                    board[y][x] = 0
                    cnt = 0
                    cnt += check_row()
                    cnt += check_col()
                    cnt += check_dia()
                    if cnt >= 3:
                        print(speak_idx)
                        exit()
