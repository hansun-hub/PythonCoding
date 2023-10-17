t=int(input())
grades = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for tc in range(1,t+1):
    n,k = map(int,input().split())
    allValue=[]
    for i in range(n):
        mid,final,hws = map(int,input().split())
        finalValue = (mid*0.35) + (final*0.45) + (hws*0.2)
        allValue.append(finalValue)

    k_value = allValue[k-1]
    allValue.sort(reverse=True)
    div = n//10
    final_k_value = allValue.index(k_value)//div

    print(f'#{tc} {grades[final_k_value]}')