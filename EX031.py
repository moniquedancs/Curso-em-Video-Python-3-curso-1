#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

#Entrada do valor da distância:
distancia = float(input("Qual é a distância que você vai percorrer? "))

#Variáveis para o cálculo da passagem de acordo com a distância:
d1 = distancia*0.50
d2 = distancia*0.45
#obs: esse cálculo poderia ser feito dentro do format

#Condição e saída:
if distancia <= 200:
    print("Sua passagem custará R${:.2f}.".format(d1))
else:
    print("Sua passagem custará R${:.2f}.".format(d2))

print("Boa viagem!") #identação que funciona para as duas situações


