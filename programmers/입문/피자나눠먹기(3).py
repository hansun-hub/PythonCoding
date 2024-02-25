
slice,n = 4,12
for i in range(1,101):
    value = slice*i
    if value-n >=0:
        pizza_num=i
        break

print(pizza_num)