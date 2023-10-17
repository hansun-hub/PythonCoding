t=int(input())
for tc in range(1,t+1):
    data = list(input())
    n=len(data)
    result=1
    for i in range(n):
        j=n-1-i
        if data[i] != data[j]:
            result=0
            break
    print(f'#{tc} {result}')
