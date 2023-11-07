
def solve(idx, sum):
    global cnt
    if idx >=n:
        return
    temp=sum+a[idx]
    if temp==k:
        cnt+=1

    solve(idx+1, sum)
    solve(idx+1, temp)


t=int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    cnt=0

    solve(0,0)
    print(f'#{tc} {cnt}')


