n=int(input())
arr=list(map(int,input().split()))
maxV = max(arr)
for i in range(n):
    arr[i]=arr[i]/maxV*100
print(sum(arr)/n)