import sys
n=int(input())

arr=[]
for _ in range(n):
    [a,b]=map(int,sys.stdin.readline().split())
    arr.append([b,a])
    
arr.sort()

for i in range(n):
    print(arr[i][1],arr[i][0])