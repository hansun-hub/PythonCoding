#D1 - 2072. 홀수만 더하기
#23/11/10

t = int(input())

for tc in range(1,t+1):
    result = 0
    lst = list(map(int,input().split()))
    for i in lst:
        if i%2!=0:
            result+=i
    print(f'#{tc} {result}')