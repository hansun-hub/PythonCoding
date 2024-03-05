t=int(input())
for _ in range(t):
    arr=input()
    stack=[]
    for i in arr:
        if i=="(":
            stack.append(i)
        elif i==")" and len(stack)!=0 and stack[-1]=="(":
            stack.pop()
        else:
            stack.append(i)
    if len(stack)==0:
        print("YES")
    else:
        print("NO")

