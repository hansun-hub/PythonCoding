n=10
answer=[]
for i in range(1,n+1):
    if i%2==0:
        continue
    else:
        answer.append(i)


print(answer)