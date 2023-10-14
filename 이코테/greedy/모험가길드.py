# n= int(input())
# data = list(map(int,input().split()))
# data.sort()
#
# result=0 # 총 그룹 개수
# count=0 #현 그룹에서의 수
#
# for i in data:
#     count+=1
#     if count>=i:
#         result+=1
#         count=0
# print(result)

n=int(input())
data = list(map(int,input().split()))
data.sort()

result=0
count=0

for i in data:
    count+=1
    # if count>=i:
