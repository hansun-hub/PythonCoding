def days_in_month(month):
    #각 월별 일수를 반환하는 함수
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    return days[month]

def count_days(m1,d1,m2,d2):
    days=0
    if m1==m2:
        days = d2-d1 +1
    else:
        days +=days_in_month(m1) -d1+1
        for month in range(m1+1,m2):
            days+=days_in_month(month)
        days+=d2
    return days


t=int(input())
for tc in range(1,t+1):
    m1,d1,m2,d2 = map(int,input().split())
    result = count_days(m1,d1,m2,d2)
    print(f'#{tc} {result}')