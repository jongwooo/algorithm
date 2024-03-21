import heapq


def solution(jobs):
    jobs.sort()
    cnt = len(jobs)
    waiting = []
    duration = []
    now = 0
    while len(duration) != cnt:
        while jobs and now >= jobs[0][0]:
            top = jobs.pop(0)
            heapq.heappush(waiting, (top[1], top[0]))
        if jobs and waiting == []:
            top = jobs.pop(0)
            now = top[0]
            heapq.heappush(waiting, (top[1], top[0]))
        x, y = heapq.heappop(waiting)
        now += x
        duration.append(now - y)
    return sum(duration) // cnt
