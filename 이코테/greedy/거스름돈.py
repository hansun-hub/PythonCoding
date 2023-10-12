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

coin_type=[500,100,50,10]

for coin in coin_type:
    n = n % coin
    count += n//coin

print(count)