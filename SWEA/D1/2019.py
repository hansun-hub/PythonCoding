n=int(input())
value=1
lst = [1]
for i in range(n):
    value*=2
    lst.append(value)

print(*lst)