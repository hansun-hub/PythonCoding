
def dfs(index,sTaste,sKcal):
    global maxTaste

    if sKcal > limit:
        return

    if sTaste > maxTaste:
        maxTaste = sTaste

    if index == n:
        return

    taste,kcal = arr[index]

    dfs(index+1,sTaste+taste,sKcal+kcal)
    dfs(index+1,sTaste,sKcal)

t=int(input())
for tc in range(1,t+1):
    n,limit = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]

    maxTaste=0
    dfs(0,0,0)
    print(f'#{tc} {maxTaste}')