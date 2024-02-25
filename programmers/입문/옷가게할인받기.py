price = 580000


if 500000 <= price:
    price-=price*0.2

elif 300000 <= price:
    price -= price * 0.1

elif 100000 <= price:
    price -= price * 0.05

print(int(price))




