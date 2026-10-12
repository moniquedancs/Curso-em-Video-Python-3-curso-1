#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

#1ª forma de resolver, mais simples:
#aluno = random.randint(1,4)
#print("O aluno escolhido para apagar o quadro é o número {} da chamada.".format(aluno))

#2ª forma de resolver, com entradas:

#Entrada dos nomes dos alunos:
a1 = input("Primeiro aluno:")
a2 = input("Segundo aluno:")
a3 = input("Terceiro aluno:")
a4 = input("Quarto aluno:")

#Armazenamento e sorteio:
lista = [a1,a2,a3,a4]
sorteio = random.choice(lista)

#Saída com o nome do aluno escolhido:
print("O aluno escolhido foi {}.".format(sorteio))