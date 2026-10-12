#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

#Entrada do valor da velocidade (em km/h):
vel = float(input("Leitura da velocidade do carro (em km/h): "))

#Variável para o cálculo do valor da multa:
multa = (vel - 80)*7

#Saída:
if vel <= 80:
    print("Você está dentro do limite de velocidade permitido de 80 km/h!")
    print("Boa viagem!")
else:
    print("Você ultrapassou o limite de velocidade permitido de 80 km/h.")
    print("Você deve pagar uma multa de R${:.2f}.".format(multa))

