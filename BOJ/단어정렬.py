import sys
n=int(input())

arr=[]
for _ in range(n):
    arr.append(sys.stdin.readline().strip())
    
arr2=set(arr)
arr=list(arr2)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)