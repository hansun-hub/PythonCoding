t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))

    result=0
    maxValue = arr[-1]
    for i in range(n-2,-1,-1):
        if maxValue < arr[i]:
            maxValue = arr[i]
        else:
            result+=maxValue-arr[i]

    print(f'#{tc} {result}')




