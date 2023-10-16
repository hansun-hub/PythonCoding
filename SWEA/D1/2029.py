t = int(input())
for tc in range(1,t+1):
    a,b = map(int,input().split())
    share = a//b
    remain = a%b
    print(f'#{tc} {share} {remain}')