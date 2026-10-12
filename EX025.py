#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

#Entrada do nome completo:
nome = str(input("Digite o seu nome completo: ")).strip()

#Saída com True/False se o nome contém "Silva":
print("Seu nome tem Silva? {}".format('SILVA' in nome.upper()))

