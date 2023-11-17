#1206. View
#11/17
T=10
for tc in range(1,T+1):
    result = 0
    houseCount = int(input())
    house = list(map(int,input().split()))
    for i in range(2,houseCount-2):
        armax = max(house[i-1],house[i-2],house[i+1],house[i+2])
        if armax<house[i]:
            result+=house[i]-armax
    print(f'{tc} {result}')
