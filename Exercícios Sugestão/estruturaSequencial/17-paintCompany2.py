import math

area = int(input("Please type the size in square meters of the wall: "))

# 1 liter per 6m²
literPaint = area / 6

# amount needed for 18 liters of paint cans
qttCan18 = math.ceil(literPaint / 18)
print("Quantity necessary of 18 liters of paint cans: ", qttCan18)

# amount needed for 3.6 liters of paint cans
qttCan3 = math.ceil(literPaint / 3.6)
print("Quantity necessary of 3.6 liters of paint cans: ", qttCan3)

# amount needed for mix of paint cans
qttL = area / 6 # take how much liters will be necessery
qttCanL = 0.1 * qttL + qttL # sum 10% of the qttL
qttCan18 = int(qttCanL / 18) # quantity of needed paint cans
qttCan3 = math.ceil(qttCanL % 18 / 3.6) # quantity of needed paint cans
print("Quantity necessary of 18 liters of paint cans: ", qttCan18)
print("Quantity necessary of 3.6 liters of paint cans: ", qttCan3)