def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if com != connect and computers[com][connect] == 1:
            if not visited[connect]:
                dfs(n, computers, connect, visited)

                
def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1
    return answer
