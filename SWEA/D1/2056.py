n = int(input())

for i in range(1,n+1):
  x =  str(input())
  year = x[0:4]
  month = x[4:6]
  day = x[6:]
  days= {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} #딕셔너리를 사용
  fail = -1

  if 0 < int(month) < 13 and int(day) <= days[int(month)]: #1~12달 사이에 맞는지 확인하고 딕셔너리를 사용해 일이 딕셔너리에 들어있는 일보다 작거나 같은지 확인 둘다 같으면 유효하므로 출력
    print("#{} {}/{}/{}".format(i,year,month,day))
  else:
    print('#{} {}'.format(i,fail))