#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

n = float(input("Digite um valor de ângulo:"))
rad = math.radians(n)
print("Para o ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}." .format(n,math.sin(rad),math.cos(rad),math.tan(rad)))

