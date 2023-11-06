for tc in range(1,11):
    #palindorme 횟수
    p=int(input())
    n=8
    arr = [list(input()) for _ in range(n)]
    count=0

    #가로
    for i in range(0,n):
        for j in range(0,n-p+1):
            if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
                count+=1

    #세로
    for j in range(0,n):
        for i in range(0,n-p+1):
            char=''
            for ci in range(i,i+p):
                char+=arr[ci][j]
            if char == char[::-1]:
                count+=1

    print(f'#{tc} {count}')

