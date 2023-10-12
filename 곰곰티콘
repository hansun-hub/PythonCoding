import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
dic_check = defaultdict(int)
answer=0

for _ in range(n):
    m = sys.stdin.readline().rstrip()
    if m=="ENTER":
        dic_check = defaultdict(int)
    else:
        dic_check[m]+=1
        if dic_check[m]==1:
            answer+=1
print(answer)
