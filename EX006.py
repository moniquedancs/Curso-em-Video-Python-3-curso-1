#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n=int(input('Digite um número:'))

#Variáveis
dobro=n*2
triplo=n*3
raiz=n**(1/2)

print('O número que você me forneceu é {}. \nSeu dobro é {} e seu triplo é {}. \nSua raíz quadrada é {:.2f}.'.format(n,dobro,triplo,raiz))