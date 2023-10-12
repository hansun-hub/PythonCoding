n=int(input())

cnt=int(n/4)
output=""
for i in range(cnt):
    cnt-=1
    output+="long "

output+="int"

print(output)