t=int(input())
for tc in range(1,t+1):
    n=int(input())
    value = ""
    for _ in range(n):
        c,k = input().split()
        k=int(k)
        value+=c*k

    print(f"#{tc}")
    for i in range(len(value)):
        if (i+1)%10 == 0:
            print(value[i])
        else:
            print(value[i],end="")
    print()