#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#1ª forma:
#import math
#n = float(input("Digite um número: "))
#print("O número {} possui o número inteiro {}." .format(n, math.trunc(n)))

#2ª forma:
from math import trunc

#Entrada do número:
n = float(input("Digite um número:"))

#Saída do número inteiro:
print("O número {} possui o número inteiro {}." .format(n,trunc(n)))