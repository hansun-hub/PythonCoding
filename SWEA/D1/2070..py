t = int(input())
for tc in range(1,t+1):
    lst = list(map(int,input().split()))
    if lst[0]>lst[1]:
        print(f'#{tc} >')
    elif lst[0]==lst[1]:
        print(f'#{tc} =')
    else:
        print(f'#{tc} <')


