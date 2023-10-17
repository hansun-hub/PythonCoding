t=int(input())
for tc in range(1,t+1):
    n=int(input())
    pascal = [n*[0] for _ in range(n)]
    pascal[0][0]=1
    for i in range(1,n):
        for j in range(n):
            if j==0:
                pascal[i][j]=1
            else:
                pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
    print(f'#{tc}')
    for k in range(n):
        for l in range(n):
            if pascal[k][l]:
                print(pascal[k][l],end=' ')
        print()