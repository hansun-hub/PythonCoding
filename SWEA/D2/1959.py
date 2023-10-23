t=int(input())
for tc in range(1,t+1):
    n,m=map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if n>m:
        n,m = m,n
        A,B = B,A

    maxSum=0
    for i in range(m-n+1):
        temp=0
        for j in range(n):
            temp+=A[j]*B[j+i]
        if temp>maxSum:
            maxSum=temp

    print(f'#{tc} {maxSum}')