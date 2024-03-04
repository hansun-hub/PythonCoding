n=int(input())
arr=[" "]*n
for i in range(n-1,-1,-1):
    j=0
    arr[i]="*"

    j+=1
    print("".join(arr))
    arr.append("*")