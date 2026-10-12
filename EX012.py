#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Entrada do preço do produto:
n=float(input('Qual é o preço do produto? R$'))

#Variável para calcular o preço com desconto:
pf=n*0.95 #Transformando porcentagem em decimal para facilitar os cálculos

#Saída do valor com desconto:
print('Com um desconto de 5%, seu produto custará {:.2f} reais.'.format(pf))