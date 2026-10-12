#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import calendar

#Entrada do ano:
ano = int(input("Digite o ano que você quer analisar: "))

#Condição e saída:
if calendar.isleap(ano): #isleap = é bissexto?
    print("O ANO {} É BISSEXTO!".format(ano))
else:
    print("O ANO {} NÃO É BISSEXTO!".format(ano))
