wageH = float(input("Please, type how much do you recieve per hour: "))
qttH = int(input("Please, type how much hours do you work in the month: "))

wage = wageH * qttH

#a
print("Salário Bruto R$ : {:.2f}" .format(wage))

#b
ir = 11/100 * wage
print("IR (11%): R$ {:.2f}" .format(ir))

#c
inss = 8/100 * wage
print("INSS (8%): R$ {:.2f}" .format(inss))

#d
sind = 5/100 * wage
print("Sindicato (5%): R$ {:.2f}" .format(sind))

#b
sl = wage - (ir + inss + sind)
print("Salário Líquido: R$ {:.2f}" .format(sl))

