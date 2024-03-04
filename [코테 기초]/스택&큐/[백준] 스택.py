import sys
n=int(input())
stack=[]
for _ in range(n):
    man=sys.stdin.readline().split()

    if man[0]=="push":
        stack.append(man[1])
    elif man[0]=="pop":
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif man[0]=="size":
        print(len(stack))
    elif man[0]=="empty":
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif man[0]=="top":
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])