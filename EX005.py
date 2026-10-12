#Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n=int(input('Digite um número:'))

#Variáveis
su=n+1
ant=n-1

print('O número que você me deu é {}. Seu sucessor é {} e o seu antecessor é {}.'.format(n,su,ant))

#Não preciso criar as variáveis su e ant. Poderia substituir direto no format, como: .format(n,(n+1),(n-1))
