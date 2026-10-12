# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

#Entrada do nome dos alunos:
a1 = input("Primeiro aluno: ")
a2 = input("Segundo aluno: ")
a3 = input("Terceiro aluno: ")
a4 = input("Quarto aluno: ")

lista = [a1,a2,a3,a4]

#1ª forma: criando uma variável
#sorteio = random.sample(lista,4)

#2ª forma: direto
random.shuffle(lista)

#Saída com a ordem de apresentação:
print("A ordem de apresentação é: {}.".format(lista))


