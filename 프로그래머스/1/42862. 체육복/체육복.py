def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    for r in reserve[:]:
        if r in lost:
            reserve.remove(r)
            lost.remove(r)
    for r in reserve:
        if r - 1 in lost:
            lost.remove(r - 1)
        elif r + 1 in lost:
            lost.remove(r + 1)
    return n - len(lost)
