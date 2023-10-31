t=int(input())
for tc in range(1,t+1):
    n=int(input())
    temp=str(n)
    arr=list(set(temp))
    multi = 2

    while True:
        multiN=n*multi
        temp2 = str(multiN)
        arr.extend(list(temp2))
        arr=list(set(arr))

        if len(arr)== 10:
            break
        multi+=1

    print(f'#{tc} {multiN}')

