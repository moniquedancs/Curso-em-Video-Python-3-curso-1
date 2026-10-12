# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

#Entrada do valor (em reais):
n=float(input('Digite seu valor, em reais:'))

#Variável com o dólar cotado no dia:
div = n/4.99

#Saída do valor (em dólar):
print('Você pode comprar {:.2f} dólares.'.format(div))