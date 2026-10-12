#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Entrada do valor (em metros):
n=float(input('Digite um valor, em metros:'))

#Variáveis de conversão:
ce=n*100 #centímetros
mi=n*1000 #milímetros

#Saída dos valores:
print('Seu valor de {} metros equivale a: \n{:.2f} centímetros. \n{:.2f} milímetros.'.format(n,ce,mi))