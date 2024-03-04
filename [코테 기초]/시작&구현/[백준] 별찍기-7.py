n=int(input())
arr=[" "]*n
arr[n-1]="*"

print("".join(arr))
for i in range(n-2,-1,-1):
    arr[i]="*"
    arr.append("*")
    print("".join(arr))

for i in range(0,n-1):
    arr[i]=" "
    arr.pop()
    print("".join(arr))