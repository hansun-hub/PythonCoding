
def dfs(count):
    global answer
    if not count:
        temp = int(''.join(values))
        if temp>answer:
            answer = temp
        return
    for i in range(length):
        for j in range(i+1,length):
            values[i],values[j] = values[j],values[i]
            temp_key = ''.join(values)
            if visited.get((temp_key,count-1),1):
                visited[(temp_key,count-1)]=0
                dfs(count-1)
            values[i],values[j] = values[j],values[i]

t=int(input())
for tc in range(1,t+1):
    value,change = input().split()
    values = list(value)
    change = int(change)
    length = len(values)
    visited = {}
    answer = -1
    dfs(change)
    print(f'#{tc} {answer}')