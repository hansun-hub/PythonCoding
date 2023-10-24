t=int(input())

dr = [0,1,0,-1]
dc = [1,0,-1,0]

for tc in range(1,t+1):
    n=int(input())

    arr = [[0]*n for _ in range(n)]

    #초기 위치와 초기 방향
    r,c = 0,0
    direction=0
    num=1

    for i in range(n*n):
        arr[r][c] = num
        num+=1

        nr, nc = r+dr[direction], c+dc[direction]

        if nr<0 or nr >=n or nc <0 or nc >=n or arr[nr][nc] != 0:
            direction = (direction+1) % 4
            nr, nc = r+dr[direction], c+dc[direction]

        r,c = nr,nc

    print(f"#{tc}")
    for row in arr:
        print(" ".join(map(str,row)))
