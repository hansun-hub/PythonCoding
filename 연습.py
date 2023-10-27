def lastday(month):
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    return days[month]


def daysreturn(m1,d1,m2,d2):
    days=0
    if m1 == m2:
        days=d2-d1+1
    else:
        days += (lastday(m1) - d1) + 1
        for i in range(m1+1,m2):
            days+=lastday(i)
        days += d2
    return days

t=int(input())
for tc in range(1,t+1):
    m1,d1,m2,d2 = map(int,input().split())
    print(f'#{tc} {daysreturn(m1,d1,m2,d2)}')
