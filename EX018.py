#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

#Entrada do valor de ângulo:
n = float(input("Digite um valor de ângulo:"))

#Variável de cálculo do ângulo em radiano, utilizando o import math:
rad = math.radians(n)

#Saída dos valores de seno, cosseno e tangente utilizando a variável rad, e outras funções de import math:
print("Para o ângulo {}, seu seno é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}." .format(n,math.sin(rad),math.cos(rad),math.tan(rad)))

