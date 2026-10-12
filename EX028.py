#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

#Variável para o computador escolher um número aleatório entre 0 e 5:
numero = random.randint(0,5)

#Entrada do usuário:
n = int(input("Eu pensei em um número entre 0 e 5. Advinhe qual é! "))

print("PROCESSANDO...")
sleep(3)

#Saída, agora com as condições if e else:
if numero == n:
    print("ACERTOU!")
else:
    print("ERROU! Eu pensei em {}.".format(numero))





