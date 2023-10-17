t=int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(n)]

    result=0
    for i in range(n):
        count=0
        for j in range(n):
            if data[i][j] == 1:
                count+=1
            if data[i][j] == 0 or j==n-1:
                if count == k:
                    result+=1
                if data[i][j]==0:
                    count=0

    for i in range(n):
        count=0
        for j in range(n):
            if data[j][i] == 1:
                count+=1
            if data[j][i] == 0 or j==n-1:
                if count == k:
                    result+=1
                if data[j][i]==0:
                    count=0

    print(f'#{tc} {result}')