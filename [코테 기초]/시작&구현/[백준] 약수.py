# def getMyDivisor(num):
#     #약수 계산기 : 1과 자기자신은 포함 X
#     lst=[]
#     for j in range(2,num):
#         if num%j==0:
#             lst.append(j)
#     return lst

n=int(input())
arr=list(map(int,input().split()))
i=1
minV=min(arr)
maxV=max(arr)
print(minV*maxV)
