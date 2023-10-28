t=int(input())
for tc in range(1,t+1):
    n=int(input())
    distance=0
    arr=[[0]*2 for _ in range(n)]

    for i in range(n):
        user_input = input().split()
        arr[i][0] = int(user_input[0])
        if len(user_input)>1:
            arr[i][1]=int(user_input[1])

    speed = 0
    for i in range(n):
        #가속
        if arr[i][0] == 1:
            speed+=arr[i][1]
            distance +=speed
        #감속
        elif arr[i][0] == 2:
            if speed!=0:
                speed-=arr[i][1]
            distance +=speed
        #현재속도유지
        elif arr[i][0] == 0:
            distance +=speed

    print(f'#{tc} {distance}')


