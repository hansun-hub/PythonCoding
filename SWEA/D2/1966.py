t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    print(f'#{tc} ',end='')
    for i in range(n):
        print(arr[i], end=' ')
    print()

