import sys

n, s, r = map(int, sys.stdin.readline().split())
damaged_teams = set(map(int, sys.stdin.readline().split()))
reserve_teams = set(map(int, sys.stdin.readline().split()))
intersection = damaged_teams & reserve_teams
damaged_teams = sorted(list(damaged_teams - intersection))
reserve_teams = list(reserve_teams - intersection)
cnt = 0
for team_num in damaged_teams:
    if team_num - 1 in reserve_teams:
        reserve_teams.remove(team_num - 1)
    elif team_num + 1 in reserve_teams:
        reserve_teams.remove(team_num + 1)
    else:
        cnt += 1
print(cnt)
