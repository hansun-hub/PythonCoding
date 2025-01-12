testCount = int(input())

final=[]
for i in range(testCount):
    repeatCount,tmp = input().split()
    repeatCount=int(repeatCount)
    tmp = list(tmp)
    result=""
    
    
    for j in range(len(tmp)):
        for k in range(repeatCount):
            result+=tmp[j]
    final.append(result)


for i in final:
    print(i)
    
        