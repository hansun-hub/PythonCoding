
def dfs(count):
    global result

    if not count:
        temp = int(''.join(values))
        if result<temp:
            result = temp
        return

    for i in range(length):
        for j in range(i + 1, length):
            values[i],values[j] = values[j],values[i]
            temp_key = ''.join(values)
            if visited.get((temp_key,count-1),1):
                visited[temp_key,count-1]=0
                dfs(count-1)
            values[j],values[i] = values[i],values[j]

t=int(input())
for tc in range(1,t+1):
    result = -1
    value, count = input().split()
    values = list(value)
    count = int(count)
    length = len(values)
    visited = {}
    dfs(count)


    print(f'#{tc} {result}')
