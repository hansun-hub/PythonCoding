n=int(input())
for _ in range(n):
    arr=input()
    stack=[]
    arr+=" "
    for i in arr:
        if i!=" ":
            stack.append(i)
        else:
            while stack:
                print(stack.pop(),end='')
            print(' ',end='')

