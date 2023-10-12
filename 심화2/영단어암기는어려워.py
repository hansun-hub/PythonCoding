from collections import defaultdict

n,m = int(input().split())
dict= defaultdict(int)

for _ in range(n):
    word=input()
    
    if len(word) < m:
        continue
    else:
        dict[word]+=1
        
answer = sorted(dict.items(), key=lambda x :(-x[1], -len(x[0]), x[0]))
answer = [i[0] for i in answer]
print(answer)