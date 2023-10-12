n = int(input())
rst=[0]*(n+1)

for i in range(0,n):
    # print("완")
    lst = map(int,input().split())
    result=0
    for j in lst:
        if j%2!=0:
            result+=j
    # print(rst[i])
    rst[i]=result

for i in range(n):
    print("#"+str(i+1)+" "+str(rst[i]))