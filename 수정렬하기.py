n = int(input())
arr=[]

for _ in range(n):
    a = int(input())
    arr.append(a)
    
arr.sort()
for i in arr:
    print(i)
    
