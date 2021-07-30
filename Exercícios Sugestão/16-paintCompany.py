import math

area = int(input("Please type the size in square meters of the wall: "))

# 1 liter per 3m²
literPaint = area / 3

# quantity necessary of can of paint
qttCan = math.ceil(literPaint / 18)

print("Quantity necessary of paint: ", qttCan)

price = qttCan * 80
print("Total price: R$ {:.2f}" .format(price))