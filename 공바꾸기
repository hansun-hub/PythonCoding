n,m = map(int,input().split())
#리스트생성
arr = [i for i in range(1,n+1)]

for _ in range(m):
    i,j = map(int,input().split())
    tmp = arr[i-1]
    arr[i-1]=arr[j-1]
    arr[j-1]=tmp
    
for i in range(n):
    print(arr[i],end=' ')