t=int(input())
for tc in range(1,t+1):
  data = input()
  year = data[:4]
  month = data[4:6]
  day = data[6:8]
  days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  fail = -1

  if 0<int(year) and 1<=int(month)<=12 and int(day)<=days[int(month)]:
    print(f'#{tc} {year}/{month}/{day}')
  else:
    print(f'#{tc} {fail}')