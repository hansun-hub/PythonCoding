t = int(input())
for tc in range(1,t+1):
    lst = list(map(int,input().split()))
    maxValue = 0
    for i in lst:
        if maxValue<i:
            maxValue=i
    print(f'#{tc} {maxValue}')