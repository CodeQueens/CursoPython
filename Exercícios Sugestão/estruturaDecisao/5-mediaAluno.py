nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if(media == 10):
    print("Aprovado com Distinção")
elif(media >= 7) and (media < 10):
    print("Aprovado")
elif(media < 7):
    print("Reprovado")
else:
    print("Nota Inválida")