n=int(input())
arr=[" "]*(2*n-1)
for i in range(len(arr)):
    arr[i]="*"

for i in range(0,n):
    print("".join(arr))
    arr[i]=' '
    arr.pop()



