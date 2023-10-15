#23.10.15
# n=1250
# count=0
#
# array = [500,100,50,10]
#
# for coin in array:
#     count+=n//coin
#     n=n%coin
#
# print(count)

n=1250
count=0

coinType = [500,100,50,10]

for i in coinType:
    count+=(n//i)
    n=n%i

print(count)
