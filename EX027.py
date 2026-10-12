#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

#Entrada do nome completo:
nome = str(input("Digite seu nome completo:")).strip()

#Variável para manipular o nome:
n1 = nome.split() #split() quebra a str em pedaços, e cada nome se torna um ítem na lista

#Saída:
print("Seu primeiro nome é: {}".format(n1[0])) #posição do primeiro nome, que começa no zero
print("Seu último nome é: {}".format(n1[len(n1)-1])) #posição do último nome
