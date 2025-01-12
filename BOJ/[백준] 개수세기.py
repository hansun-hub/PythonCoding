n=int(input())
arr = list(map(int,input().split()))

v = int(input())

cnt=0
for i in arr:
    if v==i:
        cnt+=1
print(cnt)