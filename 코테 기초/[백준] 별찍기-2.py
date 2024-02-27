n=int(input())
arr=[" "]*n
for i in range(n-1,-1,-1):
    arr[i]="*"
    print("".join(arr))