#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Entrada do comprimento das três retas:
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

#Condição:
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    triangulo = 'Sim'
else:
    triangulo = 'Não'

#Saída:
print("É possível formar esse triângulo? {}".format(triangulo))

