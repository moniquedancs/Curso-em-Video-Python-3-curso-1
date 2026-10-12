#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Entrada do número:
num = int(input("Informe um número, de 0 a 9999:"))

#Variáveis:
u = num // 1 % 10 #unidade
d = num // 10 % 10 #dezena
c = num // 100 % 10 #centena
m = num // 1000 % 10 #milhar

#Saída dos valores:
print("Esse número possui:")
print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))


