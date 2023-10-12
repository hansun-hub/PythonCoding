from collections import defaultdict
n = int(input())
arr_set = defaultdict(int)
arr_set['ChongChong']=1

for _ in range(n):
    a,b = input().split()
    
    arr_set[a] = max(arr_set[a],arr_set[b])
    arr_set[b] = max(arr_set[a],arr_set[b])
    

print(sum(arr_set.values()))
    
    