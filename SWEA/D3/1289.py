t=int(input())
for tc in range(1,t+1):
    normal = list(map(int,input()))
    init = [0 for _ in range(len(normal))]
    count=0

    for i in range(len(normal)):
        if normal[i] == init[i]:
            continue
        else:
            if normal[i] == 1:
                for j in range(i, len(normal)):
                    init[j]=1
            if normal[i] == 0:
                for j in range(i,len(normal)):
                    init[j]=0
            count+=1

    print(f'#{tc} {count}')



