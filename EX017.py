#faça um programa que leia o comprimento do cateto oposto e do cateto abjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

#Entrada dos valores de cateto:
co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente:"))

#Variável de cálculo da hipotenusa, utilizando o import math:
hi = math.hypot(co,ca)

#Saída do valor de hipotenusa:
print("A hipotenusa será: {}" .format(hi))


