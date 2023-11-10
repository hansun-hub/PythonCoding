#D2 - 1859.백만장자 프로젝트

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))

    profit=0
    maxValue=arr[-1]

    for i in range(n-2,-1,-1):
        if arr[i] > maxValue:
            maxValue = arr[i]
        else:
            profit += maxValue-arr[i]
    print(f'#{tc} {profit}')