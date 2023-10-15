n=int(input())
lst = list(map(int,input().split()))
lst.sort()

middle=len(lst)//2
print(lst[middle])
