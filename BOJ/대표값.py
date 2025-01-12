arr=[]
sum=0
for i in range(5):
    n = int(input())
    arr.append(n)
    sum+=n

#평군
print(int(sum/5))

#중앙값    
arr.sort()
print(arr[2])