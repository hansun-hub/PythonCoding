from collections import deque
n,k= map(int,input().split())

arr=deque()
for i in range(1,n+1): arr.append(i)
answer=[]

while arr:
    for _ in range(k-1):
        arr.append(arr.popleft())
    answer.append(arr.popleft())

print(str(answer).replace('[','<').replace(']','>'))
