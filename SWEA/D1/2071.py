t = int(input())

for tc in range(1,t+1):
    result = 0
    lst = list(map(int,input().split()))
    for i in lst:
        result+=i
    avg = result/len(lst)

    print(f'#{tc} {round(avg)}')