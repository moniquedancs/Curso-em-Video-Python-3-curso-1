#faça um programa que leia o comprimento do cateto oposto e do cateto abjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

co = float(input("Cateto oposto: "))
ca = float(input("Cateto adjacente:"))
hi = math.hypot(co,ca)
print("A hipotenusa será: {}" .format(hi))


