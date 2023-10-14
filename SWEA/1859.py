# T = int(input())
# for tc in range(1,T+1):
#     n = int(input())
#     lst = list(map(int,input().split()))
#
#     maxValue = lst[-1]
#     profit=0
#
#     for i in range(n-2,-1,-1):
#         if lst[i] >= maxValue:
#             maxValue = lst[i]
#         else:
#             profit += maxValue - lst[i]
#
#     # print('#{} {}'.format(tc,profit))
#     print(f'#{tc} {profit}')

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    lst = list(map(int,input().split()))

    maxValue = lst[-1]
    profit=0

    for i in range(n-2,-1,-1):
        if maxValue < lst[i]:
            maxValue = lst[i]
        else:
            profit += maxValue-lst[i]
    print(f'#{tc} {profit}')