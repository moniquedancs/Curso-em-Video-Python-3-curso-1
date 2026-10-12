#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Entrada dos três valores:
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
n3 = int(input("Terceiro valor: "))

#Condição para menor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Condição para maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

#Saída:
print("O menor número é: {}".format(menor))
print("O maior número é: {}".format(maior))

