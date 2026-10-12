#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
n=float(input('Qual é o preço do produto? R$'))
pf=n*0.95
print('Com um desconto de 5%, seu produto custará {:.2f} reais.'.format(pf))