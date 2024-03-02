n=int(input())
result=1
if n==0 or n==1:
    print(result)
else:
    for i in range(n,0,-1):
        result*=i
    print(result)