t=10
for tc in range(1,t+1):
    dump = int(input())
    box = list(map(int,input().split()))
    box.sort()
    for _ in range(dump):
        if box[-1]-box[0]<=1:
            break
        else:
            box[-1]-=1
            box[0]+=1
            box.sort()
    print(f'#{tc} {box[-1]-box[0]}')
