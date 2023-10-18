t=int(input())
for tc in range(1,t+1):
    h1,m1,h2,m2 = map(int,input().split())
    resultHour = h1 + h2
    resultMinute=m1+m2
    if resultMinute>59:
        resultMinute-=60
        resultHour+=1
    if resultHour > 12:
        resultHour -= 12

    print(f'#{tc} {resultHour} {resultMinute}')