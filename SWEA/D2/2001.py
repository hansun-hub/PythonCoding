t=int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    kills=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            fly=0
            for k in range(m):
                for l in range(m):
                    fly+=arr[i+k][j+l]
            kills.append(fly)

    print(f'#{tc} {max(kills)}')
