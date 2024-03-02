arr=[]
minv=0
hap=0
for _ in range(7):
    n=int(input())
    if n%2==1:
        arr.append(n)
if len(arr)==0:
    print(-1)
else:
    hap=sum(arr)
    minv=min(arr)
    print(hap)
    print(minv)
