t=int(input())
for tc in range(1,t+1):
    result=1
    arr=[]
    data=[list(map(int,input().split())) for _ in range(9)]
    #가로
    for i in range(9):
        arr=[]
        for j in range(9):
            if arr.count(data[i][j])>0:
                result=0
                break
            else:
                arr.append(data[i][j])
    #세로
    for i in range(9):
        arr=[]
        for j in range(9):
            if arr.count(data[j][i])>0:
                result=0
                break
            else:
                arr.append(data[j][i])
    #격자
    for i in range(0,9,3):
        for j in range(0,9,3):
            arr=[]
            for k in range(3):
                for l in range(3):
                    if arr.count(data[k][l]) > 0:
                        result = 0
                        break
                    else:
                        arr.append(data[k][l])

    print(f'#{tc} {result}')
