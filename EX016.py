#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

#import math
#n = float(input("Digite um número: "))
#print("O número {} possui o número inteiro {}." .format(n, math.trunc(n)))

from math import trunc
n = float(input("Digite um número:"))
print("O número {} possui o número inteiro {}." .format(n,trunc(n)))

