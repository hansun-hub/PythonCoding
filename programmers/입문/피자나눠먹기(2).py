
#피자 먹을 사람의 수
n,pce =4,6

#최소공배수 구하기
for i in range(1,101):
    value = n * i
    if value%6==0:
        break


answer=value//pce
print(answer)