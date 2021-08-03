numb1 = input("Informe o primeiro número: ")
numb2 = input("Informe o segundo número: ")
numb3 = input("Informe o terceiro número: ")

if numb1 > numb2 and numb1 > numb3:
    print(numb1, " é o maior número.")
elif numb2 > numb1 and numb2 > numb3:
    print(numb2, " é o maior número.")
else:
    print(numb3, " é o maior número.")