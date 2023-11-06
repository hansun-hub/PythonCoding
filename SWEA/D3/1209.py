#1209. [S/W 문제해결 기본] 2일차 - Sum

for tc in range(1,11):
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    maxVal=0

    #가로
    for i in range(100):
        vertical=0
        for j in range(100):
            vertical+=arr[i][j]
        if maxVal < vertical:
            maxVal = vertical

    #세로
    for j in range(100):
        horizon = 0
        for i in range(100):
            horizon+=arr[i][j]
        if maxVal < horizon:
            maxVal = horizon

    #대각선
    value = 0
    for i in range(100):
        value+=arr[i][i]
    if maxVal < value:
        maxVal = value

    value=0
    for i in range(100):
        value+=arr[i][100-(i+1)]
    if maxVal < value:
        maxVal = value

    print(f'#{tc} {maxVal}')
