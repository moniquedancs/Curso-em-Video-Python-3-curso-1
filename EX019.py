#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

#aluno = random.randint(1,4)
#print("O aluno escolhido para apagar o quadro é o número {} da chamada.".format(aluno))

a1 = input("Primeiro aluno:")
a2 = input("Segundo aluno:")
a3 = input("Terceiro aluno:")
a4 = input("Quarto aluno:")

lista = [a1,a2,a3,a4]

sorteio = random.choice(lista)

print("O aluno escolhido foi {}.".format(sorteio))


