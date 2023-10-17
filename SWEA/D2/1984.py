t=int(input())
for tc in range(1,t+1):
    arr=list(map(int,input().split()))
    maxV=max(arr)
    minV=min(arr)
    arr.remove(maxV)
    arr.remove(minV)
    hap=sum(arr)
    avg=0
    print(f'#{tc} {round(hap/8)}')
