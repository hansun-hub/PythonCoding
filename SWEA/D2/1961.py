t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]

    arr_90 = [[0 for i in range(n)] for _ in range(n)]
    arr_180 = [[0 for i in range(n)] for _ in range(n)]
    arr_270 = [[0 for i in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr_90[i][j] = arr[n-1-j][i]

    for i in range(n):
        for j in range(n):
            arr_180[i][j] = arr_90[n-1-j][i]

    for i in range(n):
        for j in range(n):
            arr_270[i][j] = arr_180[n-1-j][i]

    print(f'#{tc}')
    for i in range(n):
        for a in range(n):
            print(arr_90[i][a],end='')
        print(end=' ')
        for b in range(n):
            print(arr_180[i][b],end='')
        print(end=' ')
        for c in range(n):
            print(arr_270[i][c],end='')
        print()

