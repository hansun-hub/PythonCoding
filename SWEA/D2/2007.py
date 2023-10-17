t=int(input())
for tc in range(1,t+1):
    a = list(input())
    s=0

    for i in range(1,10):
        if a[0] != a[i] or a[1] != a[i+1]:
            s+=1
        else:
            break
    s+=1
    print(f'#{tc} {s}')