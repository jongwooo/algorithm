def solution(arr) : 
    x = 0
    old = arr
    while 1: 
        new = []
        for o in old : 
            if o >= 50 and o % 2 == 0:
                o //= 2
            elif o < 50 and o % 2 != 0: 
                o = o * 2 + 1
            new.append(o)
        if old == new: 
            break
        old = new
        x += 1
    return x
