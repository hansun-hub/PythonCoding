#swea. D3-2817. 부분 수열의 합
def solve(idx,sum):
    print("solve"+str(idx)+","+str(sum))
    global cnt
    if idx >= n:
        print("return 됐다")
        return
    temp = sum+A[idx]
    print("temp:"+str(temp))
    if temp==k:
        print("cnt에 1더함")
        cnt+=1

    solve(idx+1, sum)
    solve(idx+1, temp)


t=int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    cnt=0

    solve(0,0)
    print(f'#{tc} {cnt}')

