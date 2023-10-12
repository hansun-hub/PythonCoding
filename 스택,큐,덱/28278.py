import sys
from collections import deque

n = int(input())
que=deque()

for _ in range(n):
    lst = list(map(int,sys.stdin.readline().rstrip().split()))
    if lst[0]==1:
        que.append(lst[1])
        
    elif lst[0]==2:
        if que:
            print(que.pop())
        else:
            print(-1)
    
    elif lst[0]==3:
        print(len(que))
    
    elif lst[0]==4:
        if que:
            print(0)
        else:
            print(1)
            
    elif lst[0]==5:
        if que:
            print(que[-1])
        else:
            print(-1)
            
            