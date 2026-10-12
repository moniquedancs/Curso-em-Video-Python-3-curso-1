#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n=float(input('Digite um valor, em metros:'))
ce=n*100
mi=n*1000
print('Seu valor de {} metros equivale a: \n{:.2f} centímetros. \n{:.2f} milímetros.'.format(n,ce,mi))