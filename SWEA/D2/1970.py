t=int(input())

for tc in range(1,t+1):
    coin = {'50000':0, '10000':0, '5000':0, '1000':0, '500':0, '100':0, '50':0, '10':0}
    value=int(input())
    for j in coin:
        j=int(j)
        if value >= j:
            i=value//j
            value -= j * i
            j=str(j)
            coin[j]+=i
    print(f'#{tc}')
    for i in coin.keys():
        print(coin[i],end=' ')
    print()
