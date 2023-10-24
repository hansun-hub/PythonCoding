t=int(input())
for tc in range(1,t+1):
    n=int(input())

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    arr = [[0]*n for _ in range(n)]
    num=1
    direction=0
    r,c=0,0
    for i in range(n*n):
        arr[r][c]=num
        nr,nc=r+dr[direction],c+dc[direction]

        if nr<0 or nr>=n or nc <0 or nc>=n or arr[nr][nc] != 0:
            direction=(direction+1)%4
            nr, nc = r + dr[direction], c + dc[direction]

        num+=1
        r,c=nr,nc

    print(f'#{tc}')
    for row in arr:
        print(" ".join(map(str,row)))
