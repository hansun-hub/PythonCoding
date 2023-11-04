# swea D3 - 5215. 햄버거 다이어트

#sTaste -> sum Taste
#sKcal -> sum Kcal
def dfs(index, sTaste, sKcal):
    global maxTaste

    #총 칼로리를 넘으면 리턴
    if sKcal > limit:
        return

    if maxTaste < sTaste:
        maxTaste = sTaste

    if index == n:
        return

    taste, kcal = arr[index]

    dfs(index+1, sTaste+taste,sKcal+kcal)
    dfs(index+1, sTaste,sKcal)

t=int(input())
for tc in range(1,t+1):
    n,limit = map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(n)]

    maxTaste = 0
    dfs(0,0,0)

    print(f'#{tc} {maxTaste}')
