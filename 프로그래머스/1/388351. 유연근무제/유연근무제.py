def convert_time(t):
    h = t // 100
    m = t % 100
    return h * 60 + m


def solution(schedules, timelogs, startday):
    cnt = 0
    for i in range(len(schedules)):
        day = startday - 1
        schedule = convert_time(schedules[i])
        for timelog in timelogs[i]:
            if day in (5, 6):
                day = (day + 1) % 7
                continue
            time = convert_time(timelog)
            if schedule + 10 < time:
                break
            day = (day + 1) % 7
        else:
            cnt += 1
    return cnt
