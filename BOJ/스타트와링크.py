def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        power1,power2 = 0,0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    power1+=graph[i][j]
                elif not visit[i] and not visit[j]:
                    power2+=graph[i][j]
        min_diff = min(min_diff,abs(power1-power2))
        return
    
    for i in range(idx,n):
        if not visit[i]:
            visit[i]=True
            dfs(depth+1,i+1)
            visit[i]=False
            

n = int(input())

visit=[False for _ in range(n)]
graph = [list(map(int,input().split())) for _ in range(n)]

min_diff = int(1e9)

dfs(0,0)
print(min_diff)

