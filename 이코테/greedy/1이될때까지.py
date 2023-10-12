# n,k = map(int(input().split()))
# result=0
#
# while True:
#     #나눌 수 있는 수가 될 때까지 빼기
#     target=(n//k)*k
#     result+=(n-target)
#     n=target
#     #n이 k보다 작을 때 -> 더 나눌 수 없을 때 break
#     if n<k:
#         break
#     #k로 나누기
#     result+=1
#     n=n//k
#
# result+=(n-1)
# print(result)

n,k = map(int,input.split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target)
    n=target
    if n<k:
        break
    result+=1
    n //= k

result += (n-1)
print(result)

