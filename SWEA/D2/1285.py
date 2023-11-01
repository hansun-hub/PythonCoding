t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr = list(map(int,input().split()))
    minValue=100000
    count=0
    for i in arr:
        if abs(i)<minValue:
            minValue=abs(i)
            count=1
        elif abs(i)==minValue:
            count+=1

    print(f'#{tc} {minValue} {count}')